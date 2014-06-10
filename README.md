
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
1. https://github.com/scrooloose/nerdtree
2. add the following mapping in ~/.vimrc
```
:noremap <leader>nf :NERDTreeFind<CR>
```
     Command |  description
------------- | -------------
    \nf |  find currently edited buffer in the NERDTree Window
![nerdfind](/images/nerdfind.gif)

## nerdcommenter
1. https://github.com/scrooloose/nerdcommenter
2. plugin to help comment/uncomment select code block

     Command | Description 
-------------|--------------
    \cc      | Comment out the current line or text selected in visual mode
    \cu      | Uncomments the selected line(s)
![nerdcommenter](/images/nerdcommenter.gif)

## DirDiff
1. https://github.com/vim-scripts/DirDiff.vim
1. plugins to help compare diff between two directory

    Command | Description
---------------------------
 vim . -c ":DirDiff DIRECTORY_A DIRECTORY_B" | compare two directory
     s  | Sync the current diff. can also select a range and press 's' to sync
     \dj | Diff next (think j for down)
     \dk | Diff previous(think k for up)
![DirDiff](/images/dirdiff1.jpg


