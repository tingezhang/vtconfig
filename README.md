
![title](/images/matrix1.jpg)
<!--<img src="https://raw.githubusercontent.com/tingezhang/vtconfig/master/images/matrix1.jpg" alt="img text" />-->

# install
1. git clone https://github.com/tingezhang/vtconfig.git
2. cd vtconfig
3. cp configs/.vimrc configs/.tmux.conf configs/.tmux.status.conf ~/
4. mkdir -p ~/.vim/bundle
5. git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim
6. vim +PluginInstall +qall
7.  modify ~/.bashrc, add "alias tmux='tmux -2'" at the end of file
    1. alias tmux="tmux -2"
    2. alias gitlog="git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
    3. set -o vi
    4. export EDITOR=vim
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
     config  |  description
-------------|-------------
    g:startify_custom_header | config the custom header
1. https://github.com/mhinz/vim-startify
![vim-startify](/images/startify.jpg)

## vim-easymotion
     command  |  description
-------------|-------------
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
-------------|-------------
    \nf |  find currently edited buffer in the NERDTree Window
![nerdfind](/images/nerdfind.gif)

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

## YouCompleteMe
1. https://github.com/Valloric/YouCompleteMe
1. Vim Killer plugin for code completion engine
1. C/S architecture, make the completion suggestion very fast
1. Configure is a little complicated
1. Make sure Vim 7.3.584 with python2 support. some time need rebuild vim to the latest version(7.4)
    1. https://github.com/Valloric/YouCompleteMe/wiki/Building-Vim-from-source

![YouCompleteMe](/images/complete1.jpg)

## vim-markdown
1. https://github.com/plasticboy/vim-markdown
1. Syntax highlighting, matching rules and mappings for the original Markdown and extensions.

    Command | Description
------------|----------------
let g:vim_markdown_folding_disabled=1 | disable folding

## matrix
1. https://github.com/vim-scripts/matrix.vim--Yang
1. screen save for funny(the first pic)
   1. matrix和minibufexpl存在一定冲突，先:MBEClose, 再执行:Matrix

## ale

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

## Window command
1. Add the following definition in ~/.vimrc
1. use Ctrl-j, Ctrl-k, Ctrl-h, Ctrl-l to swith between windows
1. enable window selection/window resize by mouse
```
noremap <C-J>     <C-W>j
noremap <C-K>     <C-W>k
noremap <C-H>     <C-W>h
noremap <C-L>     <C-W>l

noremap <C-Down>  <C-W>j
noremap <C-Up>    <C-W>k
noremap <C-Left>  <C-W>h
noremap <C-Right> <C-W>l

:set mouse=a
:set ttymouse=xterm2
```
    Command | Description
------------|---------------
 Ctrl-W +, Ctrl-W - | adjust window row number
 Ctrl-W \>, Ctrl-W < | adjust window column number
 20 Ctrl-W [+ or =] | adjust 20 unit one time
 Ctrl-W \| | adjust window to maximum of column
 Ctrl-W _ | adjust window to maximum of row
 'x' in Tlist window | toggle TList window full screen display

## jump in files
    Command | Description
------------|--------------
    A | Cursor jump to end of line and enter 'insert' mode
    Ctrl+^ | line head(first characther of line)
    Ctrl+$ | line end
    0(zero) | column zero of line
    Ctrl+o | go back to previous edit point
    Ctrl-i | go forward to next edit point
    G | file end
    gg | file head
    Ctrl+] | jump to define in cscope + ctags
    Ctrl+t | back to pre-jump tag<within ctags and cscope>
    \\w | show beginning of word forward and then select to jump defined in easymotion
    \\b | show beginning of work backard and then select to jump defined in easymotion
    o(not zero) | enter a new line below current line and enter insert mode
    O(not zero, big cap) | enter a new line above current line and enter insert mode
    % | map 1) #if-#else-#endif 2){}
    [# | go to end of #if-#else-#endif
    ]# | go to begin of #if-#else-#endif
    [[ | jump to front of function body or front of previous function body
    [] | jump to end of function body
    ]] | jump to the front of next function body

# tmux stuff
## session relative command
 No | Commmand | Description
----|----------|--------------
 1 | tmux | open a new tmux session
 2 | tmux list-sessions | list all session exists
 3 | tmux attach -s $(session-name) | attach a session
 4 | Ctrl-a + d | detach current session 
 5 | Ctrl-a + $ | modify current session name
 6 | Ctrl-a + , | modify current window name

## window relative command
 No | Command | Description
----|---------|--------------
  1 | PREFIX + c | create a new window in current session
  2 | :exit | exit current pane/window in a session
  3 | PREFIX + , | modify current window name
  4 | PREFIX + N | switch to Nth window in current session(N is 1 to 9)
  5 | PREFIX + w | list all windows in current sessions
  6 | PREFIX + - | create a new pane in current window, split horizontal
  7 | PREFIX + | | create a new pane in current window, split vertical
  8 | PREFIX + h | move to pane above in current window
  9 | PREFIX + j | move to pane below in current window
  10| PREFIX + k | move to pane left in current window
  11| PREFIX + l | move to pane right in current window
  12| PREFIX + $ | modify session name

## work with text and buffers
1. add "setw -g mode-keys vi" in the .tmux.conf file

    Command | Description
------------|-----------------
    PREFIX + [ | enter copy mode
    h,j,k,l | same as shortcut in vim
    ENTER | exit copy mode
    Ctrl-b, Ctrl-f, g, G | move page, top, bottom
    ? | search backward in the buffer, edit search pattern and press ENTER
    n | jump to next match item
    N | jump to previous match item
    / | search forward through the buffer
    SPACE .. ENTER | press SPACE, and the move the cursor to the end of the text, and presss ENTER to copy
    PREFIX + ] | paste
    cmd: capture-pane | capture a pane
    cmd: show-buffer | show buffer content
    cmd: save-buffer[FILE_NAME] | output buffer into file
    cmd: list-buffers, PREFIX + = | list all past bufers and paste selected buffer contents

## mouse operation config
1. Mouse support - set to on if you want to use the mouse
```
setw -g mode-mouse on
set -g mouse-select-pane on
set -g mouse-resize-pane on
set -g mouse-select-window on
```
# config for .bashrc
1. alias tmux="tmux -2"
1. alias gitlog="git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"

# Tmux Plugin Manager
1. git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm
1. Put this at the bottom of .tmux.conf
    1. {{{
    # List of plugins
    set -g @plugin 'tmux-plugins/tpm'
    set -g @plugin 'tmux-plugins/tmux-sensible'
    set -g @plugin 'tmux-plugins/tmux-resurrect'
    set -g @plugin 'tmux-plugins/tmux-sessionist'

    # Initialize TMUX plugin manager (keep this line at the very bottom of tmux.conf)
    run '~/.tmux/plugins/tpm/tpm'
    }}}
1. install: hit prefix + I (I as in Install) to fetch the plugin
1. uninstall: hit prefix + alt + u (u as in uinstall) to remove the plugin

# memect
![memect](/images/memect.jpg)

1. www.memect.com is a web service targeted memory connection, have many topics 
    1. http://u.memect.com/vim    for vim topic
    2. http://u.memect.com/emacs/ for emacs topic
    3. http://u.memect.com/daijian/ for big data topic

