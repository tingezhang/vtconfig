
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
2. plugins to help compare diff between two directory


     Command | Description 
-------------|--------------
 vim . -c ":DirDiff DIRECTORY_A DIRECTORY_B" | compare two directory
     s  | Sync the current diff. can also select a range and press 's' to sync
     \dj | Diff next (think j for down)
     \dk | Diff previous(think k for up)
![DirDiff](/images/dirdiff1.jpg)

## EasyGrep
1. https://github.com/vim-scripts/EasyGrep
2. based on ":vimgrep" command to find tag under cursor easily

     Command | Description 
-------------|--------------
<Leader>vv(double v) | Grep for the word under curosr
![EasyGrep](/images/easygrep1.jpg)

## Gundo
1. https://github.com/sjl/gundo.vim
1. Gundo.vim is Vim plugin to visualize your Vim undo tree.
1. Add the following mapping in ~/.vimrc
```
nnoremap <F6> :GundoToggle<CR>
```
     Command | Description 
-------------|--------------
    F6 | Togglee undo window
![Gundo](/images/gundo1.jpg)

## Ctrl-P
1. https://github.com/kien/ctrlp.vim
1. Full path fuzzy file, buffer, mru, tag, ... finder for Vim.

    Command | Description
------------|---------------
    Ctrl-p | invoke CtrlP in find file mode
    Ctrl-f , Ctrl-b | cycle between tree modes(Find files, Find Buffer, Find MRU)
    Ctrl-d | switch to filename only search instead of full path
    Ctrl-j | to navigate in the result list

![CtrlP](/images/ctrlp1.jpg)

## vim-bookmarks
1. https://github.com/MattesGroeger/vim-bookmarks
1. bookmaks which works independently from vim marks
1. add the following config into .vimrc
```
let g:bookmark_sign = '♥'
let g:bookmark_highlight_lines = 1
highlight BookmarkSign ctermbg=166 ctermfg=89
highlight BookmarkAnnotationSign ctermbg=30  ctermfg=89
highlight BookmarkLine ctermbg=166 ctermfg=NONE
highlight BookmarkAnnotationLine ctermbg=30  ctermfg=NONE
```

    Command | Description
------------|---------------
    mm | Add/Remove bookmark at current line
    mi | Add/Edit/Remove annotation at current line
    ma | Show all bookmarks
    mn | Jump to next bookmark in buffer
    mp | Jump to previous boookmark in buffer
    mc | Clear bookmarks in current buffer only
    mx | Clear bookmarks in all buffer

![vim-bookmarks](/images/bookmarks1.jpg)


## vim-multiple-cursors
1. https://github.com/terryma/vim-multiple-cursors
1. https://github.com/terryma/vim-multiple-cursors

    Command | Description
------------|----------------
    Ctrl-n | select next key
    Ctrl-p | in **Visual** mode will remove the current virtual cursor and go back to the previous virtual cursor location.
    Ctrl-x | in **Visual** mode will remove the current virtual cursor and skip to the next virtual cursor location.

![vim-multiple-cursors](/images/m_cursor_final.jpg)


## YouCompleteMe
1. https://github.com/Valloric/YouCompleteMe
1. Vim Killer plugin for code completion engine
1. C/S architecture, make the completion suggestion very fast
1. Configure is a little complicated
1. Make sure Vim 7.3.584 with python2 support. some time need rebuild vim to the latest version(7.4)
    1. https://github.com/Valloric/YouCompleteMe/wiki/Building-Vim-from-source

![YouCompleteMe](/images/complete1.jpg)


## syntastic
1. https://github.com/scrooloose/syntastic
1. Syntastic is a syntax checking plugin for Vim that runs files through external syntax checkers and displays any resulting errors to the user
1. following picture is from his github
![syntastic](/images/screenshot_1.png)


## vim-markdown
1. https://github.com/plasticboy/vim-markdown
1. Syntax highlighting, matching rules and mappings for the original Markdown and extensions.

    Command | Description
------------|----------------
let g:vim_markdown_folding_disabled=1 | disable folding

## matrix
1. https://github.com/vim-scripts/matrix.vim--Yang
1. screen save for funny

# useful commands

## buffer operation
 No | Command | example
----|---------|----------
 1 | :buffers | show all buffers(the same as :ls)
 2 | :buffer 2(b2) | show buffer 2
 3 | :bf | buffer first: show first buffer
 4 | :bn | buffer next: show next buffer
 5 | :bp | buffer previous: show previous buffer
 6 | :bd 3 | buffer delete: delete buffer 4
 7 | :bufdo[1]{cmd} | Execute{cmd} in each buffer in the buffer list
 8 | :sb[n] | split window to show buffer [N] in horizontal mode
 9 | :e# | edit the last edit buffer
