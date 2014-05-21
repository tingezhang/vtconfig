set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'gmarik/Vundle.vim'
Plugin 'Lokaltog/powerline'
Plugin 'bling/vim-airline'
"Plugin 'bling/vim-bufferline'
Plugin 'Lokaltog/vim-easymotion'
Plugin 'Lokaltog/vim-distinguished'
Plugin 'scrooloose/nerdtree'
Plugin 'vim-scripts/winmanager'
Plugin 'taglist.vim'
Plugin 'DirDiff.vim'
Plugin 'fholgado/minibufexpl.vim'
Plugin 'vim-scripts/genutils'
Plugin 'vim-scripts/lookupfile'
Plugin 'sjl/gundo.vim'
Plugin 'kien/ctrlp.vim'
Plugin 'mhinz/vim-startify'
"Plugin 'edkolev/tmuxline.vim'
Plugin 'tomasr/molokai'
Plugin 'vim-scripts/peaksea'
"Plugin 'brookhong/cscope.vim'
Plugin 'Rykka/colorv.vim'
Plugin 'vim-scripts/EasyGrep'
"Plugin 'CCTree'
"Plugin 'hari-rangarajan/CCTree'
"Plugin 'terryma/vim-multiple-cursors'
Plugin 'kien/rainbow_parentheses.vim'
Plugin 'MattesGroeger/vim-bookmarks'



" The following are examples of different formats supported.
" Keep Plugin commands between vundle#begin/end.

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required
" To ignore plugin indent changes, instead use:
"filetype plugin on
"
" Brief help
" :PluginList          - list configured plugins
" :PluginInstall(!)    - install (update) plugins
" :PluginSearch(!) foo - search (or refresh cache first) for foo
" :PluginClean(!)      - confirm (or auto-approve) removal of unused plugins
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line

:set t_Co=256

let g:NERDTree_title="[NERD Tree]"
let g:winManagerWindowLayout='NERDTree|TagList'
function! NERDTree_Start()
	exec 'NERDTree'
endfunction
function! NERDTree_IsValid()
	return 1
endfunction

nmap wm :if IsWinManagerVisible() <BAR> WMToggle<CR> <BAR> else <BAR> WMToggle<CR>:q<CR> endif <CR><CR>

"colorscheme distinguished
colorscheme molokai


syntax enable
syntax on
set showmatch
set number
set hlsearch
set laststatus=2
set ts=4
set sw=4
set expandtab
set ignorecase
set fileformat=unix
set list
set listchars=tab:>-,trail:-

set nocp

let g:miniBufExplMapWindowNavVim = 1
let g:miniBufExplMapWindowNavArrows = 1
let g:miniBufExplMapCTabSwitchBufs = 1
let g:miniBufExplModSelTarget = 1

" key map for session
:nmap sl :SessionList<CR>
:nmap ss :SessionSave<CR>
:nmap sc :SessionClose<CR>

:map <F7> <Esc>A("%s,%d \n", __FUNCTION__, __LINE__);<Esc>bbbbbbb

" key map for cscope
:nmap <C-f>s :cs find s <C-R><C-W><CR>
:nmap <C-f>g :cs find g <C-R><C-W><CR>
:nmap <C-f>c :cs find c <C-R><C-W><CR>
:nmap <C-f>t :cs find t <C-R><C-W><CR>

:set ruler
:set t_Co=256
:highlight ColorColumn ctermbg=239
:set colorcolumn=80

set cursorline

set noswapfile

:set mouse=a

let g:airline_powerline_fonts = 1
set laststatus=2
let g:airline_detect_whitespace          = 0
let g:airline#extensions#tabline#enabled = 1
let g:airline#extensions#tabline#buffer_nr_show = 1
let g:airline_theme = "molokai"
let g:airline#extensions#bufferline#enabled = 1
let g:airline#extensions#tmuxline#enabled = 0



if !exists('g:airline_symbols')
    let g:airline_symbols = {}
endif

let g:startify_custom_header = [
\ '                                                                                                              ',
\ '                                            .;===============,                  :;========+=====;.    ..      ',
\ '                                          Y##XXRRRRRRRRRRRRRV##              =###XRRRBRRRRRRRBRXM#. iYRXIi    ',
\ '                                        X####                ##            +####i                #. tVVYYi    ',
\ '                                     .R######                ##          t######t               ,#   ..,      ',
\ '                                   ,M########                ##        I########t               :#            ',
\ '                                 ;W##########                ##      V##########t               ,#            ',
\ '                               =#############                ##    X############t               :#            ',
\ '                             i###############                #B  B##############t               ,#            ',
\ '                           I#################                B#X################t               ,#.           ',
\ '                         V###################                V##################t               .#.           ',
\ '                       X####################MIVVXVXXXVXVVB#WM##################MXYVVXXXVXVXVXXXYX#            ',
\ '                    .B####################= YYYVYVYVYYYYY####################X iYYYVVVYVYVYVVVYYYR            ',
\ '                  :M####################+  :#i++i+i==;;:;,.  V#############V   ##=++iii+iii+i+i+V#.           ',
\ '                ;#####################;     IXXXXXXR#####################Y     iYXXRXRXRXRXRXRXXVY            ',
\ '              +####################M:      =#i+;;:;:=;=;=;;;:R#########t       #W=i+iii+iii+iii+Y#.           ',
\ '            i####################B.        ,#iiBBBBBRRRRRRRRVW#######i         MXiititititttitiiI#            ',
\ '          Y####################X            RtX####################=           VXIYYYYYYYYYYYYYIYB            ',
\ '       ,B####################V             R#t=;:;:;:;:;:;::,W###=             ##IIYIYIYIYYYYYIIB#,           ',
\ '     .R####################Y             i####################W:               ;++i+i+i+i+i+i+i++=            ',
\ '                                                                                                              ',
\ '                                                                                                              ',
\ '                                                                                                              ',
\ '     .=;   ,+;           =:           =;=;:        ,i    +:       :;=;+,        :=           :=     ,;+=;.    ',
\ '     +BXt  RVB          tXX;         .MI,=Wi       .RR  IB.       IB==+,        IB           IB     +ii+++    ',
\ '     =R X=V;=R         iM:tM:         Rt+Xi          RI=B         tX;;+         tX           tR      ::::     ',
\ '     +B .MY +B        iB;:,tB;       .B= IV,         .RB,         tR=+i=        tBitt        tRiit            ',
\ '                                                                                                              ',
\ '                                                                                                              ',
\ '                                                                                                              ',
\]

set backspace=indent,eol,start " backspace over everything in insert mode

nmap <leader>fb :%!xxd -g1 <CR> :%s/^.\{9\}//g <CR> :%s/.\{18\}$//g <CR> :%s/0a *\%$//g<CR> :g/^$/d<CR> :%s/^/0x/g<CR>  :%s/ /,0x/g<CR> :1,$-1s/$/,/g<CR>


au VimEnter * RainbowParenthesesToggle
au Syntax * RainbowParenthesesLoadRound
au Syntax * RainbowParenthesesLoadSquare
au Syntax * RainbowParenthesesLoadBraces
