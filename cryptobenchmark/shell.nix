{ pkgs ? import <nixpkgs> {} }:
with pkgs;
mkShell {
  nativeBuildInputs = [ openssl openssl.dev pkg-config ];
  shellHook = ''
    export LD_LIBRARY_PATH=${stdenv.cc.cc.lib}/lib:$LD_LIBRARY_PATH
    export PKG_CONFIG_PATH=${pkgs.openssl.dev}/lib/pkgconfig;
  '';
}
