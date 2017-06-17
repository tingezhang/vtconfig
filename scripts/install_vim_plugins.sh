git clone https://github.com/tingezhang/vtconfig.git
cd vtconfig
cp configs/.vimrc configs/.tmux.conf configs/.tmux.status.conf ~/
mkdir -p ~/.vim/bundle
git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim
vim +PluginInstall +qall
