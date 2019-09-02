{ config, pkgs, ... }:

{
  imports =
    [
      ./hardware-configuration.nix
      ./home-manager/nixos
    ];

  # System channel
  system.stateVersion = "19.03";

  # Bootloader
  boot.loader.systemd-boot.enable = true;
  boot.loader.efi.canTouchEfiVariables = true;
  # Ensure newer kernel is used
  boot.kernelPackages = pkgs.linuxPackages_latest;

  # Hostname
  networking.hostName = "silvus-laptop";
  # WiFI configuration
  #
  # Connect to new Wifi network:
  # wpa_cli -g /run/wpa_supplicant/[interface]
  # > scan
  # > scan_results
  # > add_network
  # 0
  # > set_network 0 ssid "SSID"
  # > set_network 0 psk "PSK" # For network with PSK
  # > set_network 0 key_mgmt NONE # For network without PSK
  # > enable_network 0
  # > save_config
  # 
  # This is not done deterministically to ensure that the Nixos does not need
  # to be secret.
  networking.wireless = {
    enable = true;
  };


  # Select internationalisation properties.
  i18n = {
    consoleFont = "Lat2-Terminus16";
    consoleKeyMap = "de";
    defaultLocale = "en_US.UTF-8";
  };

  # Timezone
  time.timeZone = "Europe/Berlin";
  # Provide dual boot compatability with Windows
  time.hardwareClockInLocalTime = true;

  # Sound
  sound.enable = true;
  hardware.pulseaudio.enable = true;


  # User accounts
  users.users.silvus = {
    group = "silvus";
    isNormalUser = true;
    extraGroups = [ "wheel" ]; # Enable ‘sudo’ for the user.
  };
  users.groups.silvus = {};


  # XServer config
  services.xserver = {
    enable = true;

    # Enable touchpad support.
    libinput.enable = true;
    # Manually configure touchpad and trackpoint speed
    # Cannot be done using Nixos libinput configuration because it only supports a single input device
    config = ''
      Section "InputClass"
        Identifier "Additional configuration Touchpad"
        MatchIsTouchpad "on"
        Driver "libinput"
        Option "AccelSpeed" "0.4"
      EndSection
      Section "InputClass"
        Identifier "Additional configuration trackpoint"
        MatchisPointer "on"
        Driver "libinput"
        Option "AccelSpeed" "-0.5"
      EndSection
    '';

    # Keyboard layout
    layout = "de";

    # Monitor specific configuration
    xrandrHeads = [
      {
        # Internal screen
        output = "eDP-1";
        primary = true;
        # Ensures around 125 DPI
        monitorConfig = "DisplaySize 407 228";
      }
    ];

    # Required packages
    displayManager.lightdm.enable = true;
    windowManager.i3.enable = true;
    windowManager.i3.package = pkgs.i3-gaps;
  };

  # Required for brightness control
  programs.light.enable = true;
  # Service for setting up global keybinds
  services.actkbd = {
    enable = true;
    # Keycodes can sometimes be determined using `xev -event keyboard`. If they
    # are not detected it might be because actkbd detects them differently. In
    # that case you can use `actkbd -v9 -d [device]`.
    bindings = [
      # Control brightness
      # light -r enables raw mode, (at least here) the maximum brightness is
      # 255. This allows comfortable usage of increments of 16 without large
      # distortions which happen when using percentwise increments.
      {
        keys = [ 224 ];
        events = [ "rel" ];
        command = "/run/current-system/sw/bin/light -rU 16";
      }
      {
        keys = [ 225 ];
        events = [ "rel" ];
        command = "/run/current-system/sw/bin/light -rA 16";
      }
      # Volume and playback control has to be done at user level, that is using
      # i3.
    ];
  };



  # Import user specific configuration
  home-manager.users.silvus = { pkgs, ... }: {
    imports = [
      ./i3/i3.nix
      ./i3blocks/i3blocks.nix
      ./termite.nix
      ./vim/vim.nix
    ];
    # Allow all software to be installed
    nixpkgs.config.allowUnfree = true;
    # User packages
    home.packages = with pkgs; [
      firefox 
      # Vivaldi requires proprietary codecs to play some media (e.g. Twitch, 
      # ...). They have to be installed separately. Vivaldi prints a command to
      # stdout on startup that can be used for this.
      vivaldi
      discord spotify
      git
      wget curl
      htop
    ];
  };
}
