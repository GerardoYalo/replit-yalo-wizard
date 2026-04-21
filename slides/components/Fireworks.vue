<script setup>
import { onMounted, onUnmounted, ref } from 'vue'
import confetti from 'canvas-confetti'

const el = ref(null)
let alreadyFired = false

onMounted(() => {
  const checkVisibility = setInterval(() => {
    if (!el.value) return
    
    const style = window.getComputedStyle(el.value)
    
    // Verify it's not hidden via CSS
    if (parseFloat(style.opacity) > 0.5 && !alreadyFired) {
        
        // Verify it's actually in the active viewport (not just pre-rendered offscreen)
        const rect = el.value.getBoundingClientRect()
        const inViewport = (
          rect.top >= -100 &&
          rect.left >= -100 &&
          rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) + 100 &&
          rect.right <= (window.innerWidth || document.documentElement.clientWidth) + 100
        )

        // Slidev has fixed layout scaling, so as long as it's within viewport bounds
        // and the opacity is high (meaning v-click is active), we fire!
        if (inViewport && rect.width > 0) {
            alreadyFired = true
            
            const duration = 3 * 1000;
            const end = Date.now() + duration;

            (function frame() {
              confetti({
                particleCount: 8,
                angle: 60,
                spread: 55,
                origin: { x: 0 },
                colors: ['#EEAE3D', '#EC4899', '#06B6D4', '#ffffff']
              });
              confetti({
                particleCount: 8,
                angle: 120,
                spread: 55,
                origin: { x: 1 },
                colors: ['#EEAE3D', '#EC4899', '#06B6D4', '#ffffff']
              });

              if (Date.now() < end) {
                requestAnimationFrame(frame);
              }
            }());
        }
    }
  }, 200)

  onUnmounted(() => {
    clearInterval(checkVisibility)
  })
})
</script>

<template>
  <div ref="el" class="absolute w-2 h-2 top-1/2 left-1/2"></div>
</template>
