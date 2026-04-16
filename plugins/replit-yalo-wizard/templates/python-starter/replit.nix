{ pkgs }:
pkgs.mkShell {
  buildInputs = [
    pkgs.python311Full
    pkgs.gcc
    pkgs.stdenv.cc.cc.lib
    pkgs.uv
  ];
  shellHook = ''
    export LD_LIBRARY_PATH="${pkgs.stdenv.cc.cc.lib}/lib:$LD_LIBRARY_PATH"
  '';
}
