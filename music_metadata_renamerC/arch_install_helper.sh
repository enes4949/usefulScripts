#/bin/sh
user="archie"
userPass=""
rootPass=$user

# add user
useradd -m -G wheel $user
passwd $userPass
chmod 700 /home/$user
chown $user /home/$user
cd /home/$user
echo '%wheel ALL=(ALL:ALL) ALL' | sudo EDITOR='tee -a' visudo
echo '%wheel ALL=(ALL:ALL) NOPASSWD: /usr/bin/protonvpn' | sudo EDITOR='tee -a' visudo # make protonvpn not to ask password

# Initilize git and copy repos
pacman -Syu git openssh
su $user
cd /home/$user
ssh-keygen -t rsa -b 4096 -f .ssh/id_rsa -N ""
key=$(cat .ssh/id_rsa.pub)
curl -H "Authorization: token ${token}" --data '{"title":"test-key1","key":"'"${key[@]}"'"}' https://api.github.com/user/keys
git clone git@github.com:enes4949/dwm.git
git clone git@github.com:enes4949/scripts.git .local/bin
git clone git@github.com:enes4949/share.git .local/bin
git clone git@github.com:enes4949/slstatus.git
git clone git@github.com:enes4949/st.git
git clone git@github.com:enes4949/dotfiles.git .config
git clone git@github.com:enes4949/mozilla.git .mozilla
git clone git@github.com:enes4949/etc.git /etc
git clone git@github.com:enes4949/boot.git /boot

# install yay
git clone git@github.com:Jguer/yay.git
cd yay
makepkg -si
cd ..

# set basic system settings
su
passwd $rootPass
ln -sf /usr/share/zoneinfo/Europe/Istanbul /etc/localtime
hwclock --systohc
locale-gen
echo "LANG=en_US.UTF-8" >/etc/locale.conf
echo "trq" >/etc/vconsole.conf
echo "PC" >/etc/hostname
yay -Syu $(cat /home/user/.config/packages)
