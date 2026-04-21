<script setup>
import { onMounted, onUnmounted, ref } from 'vue'

const canvasRef = ref(null)

onMounted(() => {
  const canvas = canvasRef.value
  const ctx = canvas.getContext('2d')
  const parent = canvas.parentElement
  
  let width = parent.clientWidth || window.innerWidth
  let height = parent.clientHeight || window.innerHeight
  
  const dpr = window.devicePixelRatio || 1
  canvas.width = width * dpr
  canvas.height = height * dpr
  ctx.scale(dpr, dpr)

  const stars = []
  const numStars = 150

  for (let i = 0; i < numStars; i++) {
    stars.push({
      x: Math.random() * width,
      y: Math.random() * height,
      z: Math.random() * 2 + 0.5,
      opacity: Math.random() * 0.7 + 0.3,
      speedScale: Math.random() * 0.5 + 0.5
    })
  }

  let animationFrameId
  let time = 0
  
  const render = () => {
    time += 0.05
    ctx.clearRect(0, 0, width, height)
    
    stars.forEach(star => {
      // Parallax upward movement: deeper stars move slower
      star.y -= (0.15 + star.z * 0.1) * star.speedScale
      
      // Horizontal drift based on sin wave
      star.x += Math.sin(time + star.z) * 0.05 * star.speedScale

      if (star.y < 0) {
        star.y = height + 10
        star.x = Math.random() * width
      }
      if (star.x < 0) star.x = width
      if (star.x > width) star.x = 0
      
      // Twinkle
      const currentOpacity = Math.max(0.1, Math.min(1, star.opacity + Math.sin(time * star.speedScale) * 0.3))
      
      ctx.beginPath()
      ctx.arc(star.x, star.y, star.z, 0, Math.PI * 2)
      ctx.fillStyle = `rgba(238, 174, 61, ${currentOpacity * 0.6})` // Yalo Orange tint
      ctx.fill()
      
      // Inner bright white core
      ctx.beginPath()
      ctx.arc(star.x, star.y, star.z * 0.5, 0, Math.PI * 2)
      ctx.fillStyle = `rgba(255, 255, 255, ${currentOpacity})`
      ctx.fill()
    })
    
    animationFrameId = requestAnimationFrame(render)
  }
  
  render()
  
  onUnmounted(() => {
    cancelAnimationFrame(animationFrameId)
  })
})
</script>

<template>
  <div class="absolute inset-0 overflow-hidden z-0 pointer-events-none opacity-50 mix-blend-screen">
    <canvas ref="canvasRef" style="width: 100%; height: 100%;"></canvas>
  </div>
</template>
