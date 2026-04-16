{ pkgs }: {
  deps = [
    pkgs.uv
    pkgs.python311
    pkgs.stdenv.cc.cc.lib
  ];
  env = {
    LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
      pkgs.stdenv.cc.cc.lib
    ];
  };
}
