{ config, lib, pkgs, ... }:

{
  home.packages = with pkgs; [ 
    i3-gaps
    xorg.xsetroot
    dejavu_fonts
  ];

  home.file.".config/i3/config".source = ./config;
}
