{ config, lib, pkgs, ... }:

{
  home.packages = with pkgs; [ 
    i3blocks
    acpi python3 sysstat
  ];

  home.file.".config/i3blocks/config".source = ./config;
  home.file.".config/i3blocks/scripts".source = ./scripts;
}
