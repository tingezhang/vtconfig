
![title](/images/matrix1.jpg)
<!--<img src="https://raw.githubusercontent.com/tingezhang/vtconfig/master/images/matrix1.jpg" alt="img text" />-->

# install
1. git clone https://github.com/tingezhang/vtconfig.git
2. cd vtconfig
3. cp configs/.vimrc configs/.tmux.conf configs/.tmux.status.conf ~/
4. mkdir ~/.vim/bundle
5. git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim
6. vim +PluginInstall +qall
7.  modify ~/.bashrc, add "alias tmux='tmux -2'" at the end of file
8. install font for status line:
    1. git clone https://github.com/runsisi/consolas-font-for-powerline
    2. put all font into system font directory
    3. config putty or terminal to use powerline-consola font to


# config for plugins
1. some configs/tips for some pop plugins

## vundle
1. plugin to manager other plugins, make plugins installation/remove very easily
2. https://github.com/gmarik/Vundle.vim
3. install command "vim +PluginInstall +qall"
![vundle install UI](/images/vundle.jpg)

## vim-startify
     config   |  description
------------- | -------------
    g:startify_custom_header | config the custom header
1. https://github.com/mhinz/vim-startify
![vim-startify](/images/startify.jpg)

## vim-easymotion
     command  |  description
------------- | -------------
      \\w | beginning of word forward
      \\b | beginning of word backward
      \\e | end of word forward
      \\ge | end of word backward
      \\j | line downward
      \\k | line upward
1. https://github.com/Lokaltog/vim-easymotion
![vim-easymotion](/images/easymotion_2.jpg)

## nerdtree
add the following mapping in ~/.vimrc
```
:noremap <leader>nf :NERDTreeFind<CR>
```
