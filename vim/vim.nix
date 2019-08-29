{ config, lib, pkgs, ... }:

{
  home.packages = with pkgs; [ 
    (vim_configurable.override { python = python3; })
    python3 git ag 
  ];

  home.file.".vimrc".source = ./vimrc;
}
