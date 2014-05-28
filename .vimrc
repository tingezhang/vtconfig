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
Plugin 'Lokaltog/vim-easymotion'
"Plugin 'junegunn/vim-easy-align'
Plugin 'Lokaltog/vim-distinguished'
Plugin 'scrooloose/nerdtree'
Plugin 'vim-scripts/winmanager'
Plugin 'taglist.vim'
Plugin 'DirDiff.vim'
Plugin 'fholgado/minibufexpl.vim'
Plugin 'vim-scripts/genutils'
Plugin 'vim-scripts/lookupfile'
Plugin 'vim-scripts/EasyGrep'
Plugin 'itchyny/calendar.vim'
Plugin 'sjl/gundo.vim'
Plugin 'kien/ctrlp.vim'
Plugin 'mhinz/vim-startify'
Plugin 'tomasr/molokai'
Plugin 'vim-scripts/peaksea'
Plugin 'kien/rainbow_parentheses.vim'
Plugin 'MattesGroeger/vim-bookmarks'
Plugin 'scrooloose/nerdcommenter'
Plugin 'vim-scripts/sessionman.vim'
Plugin 'vim-scripts/AnsiEsc.vim'
"Plugin 'Valloric/YouCompleteMe'
"Plugin 'scrooloose/syntastic'
Plugin 'terryma/vim-multiple-cursors'
Plugin 'vim-scripts/matrix.vim--Yang'

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

"set cursorline

set noswapfile

let g:airline_powerline_fonts = 1
set laststatus=2
let g:airline_detect_whitespace          = 0
let g:airline#extensions#tabline#enabled = 1
let g:airline#extensions#tabline#buffer_nr_show = 1
let g:airline_theme = "molokai"
let g:airline#extensions#bufferline#enabled = 1
let g:airline#extensions#tmuxline#enabled = 0

:set mouse=a
:set ttymouse=xterm2
:set backspace=indent,eol,start

if !exists('g:airline_symbols')
    let g:airline_symbols = {}
endif

let g:startify_custom_header = [
            \ '                                                                                                                                  ',
            \ '                                                          ,r7S2222SXr;:,                                                          ',
            \ '                                                    .ra88a2XX7XX2a8B@@MMMMMW2                                                     ',
            \ '                                                 ,SWMMMMB8ZZSSXrrrrXa80X:i;S02iri                                                 ',
            \ '                                               XWM@S;.. ,:;72ZBB@WW@M@@0  7Z0WMMMM0i                                              ',
            \ '                                             S@MM@@M@W082Xr;:i;X20a;i, X0@WWW@000BWM0.                                            ',
            \ '                                           ,WMBXrii:;rX280@MMWWWWB@0  2BBWM87.iB@B00@M7                                           ',
            \ '                                          rMW082X;:.       :S0ZaSa2;rWWBWS   aM0;.0W0BM2                                          ',
            \ '                                         rMB8880WWMMMMMMM@@BBB0ar  ;MBBZ, rWMS   8MXaB@MX                                         ',
            \ '                                        .M08Z80W@M@@BB000BBWWW@MM; MWZZaZWMS   ZB7  W@;ZM                                         ',
            \ '                                        0W0ZB@@ar.                 .,X00B0a:SWMi  SM2  0MX                                        ',
            \ '                                       .MB80@X             ,,,     .BM@0a00W@0  aMW: XMMM:                                        ',
            \ '                                       :M80W7      ir;r, .7;rrr    WM8;;BB@BZZ0MMB8a@MZ:                                          ',
            \ '                                       ,MB0W       7;;;7,.;;i;r,       BW8r,WMW2  :7   7BM,                                       ',
            \ '                                        @@MZ ;rr;: ,ri;ir:;;;i;;        ,   i     iMM.MMBM2                                       ',
            \ '                                        ;MM. r;;;ri,i;;;i; ir;i7,   ,@MMMMM7 aMMMM @M;XiM8                                        ',
            \ '                                          .. .;;;i;;i.;r;;. :r;ir.  iW2  XMM,MW :MaMM   r                                         ',
            \ '                                           Xr;i,iri;;, ,;7r  .r;;7,     7MM  WMWMM   ,ir;i                                        ',
            \ '                                           .7;r. .;rrr,  i7r   r;iri  aMMM:iWW     :;r7;,                                         ',
            \ '                                             rrri  .;rri  ,7r:  ;;;r;.r0W@MM@;  .;;rri.                                           ',
            \ '                                              :r7r:  .;rr.  rr;.,;ii;;:       i;r;7;.                                             ',
            \ '                                                i777:  :;ri.,;iri;iiiiiiiii;;;;;;r,                                               ',
            \ '                                                  ,;77;:;i;;;i;iiiiiiiiiiiiiii;;;                                                 ',
            \ '                                                     irriii;iiiiiii;iiiiiiiii;r;                                                  ',
            \ '                                                       ,;;iiiiiiiiiiiiiiiiii;;;                                                   ',
            \ '                                                       i ,;;iiiiiiiii;iiiii;;r                                                    ',
            \ '                                                       ,B  iriiiiiiiii;iiiii7,                                                    ',
            \ '                                                        XM. ,;i;iiiiiiiiiii;;                                                     ',
            \ '                                                         MMr  r;;iiiiiiiiii;i                                                     ',
            \ '                                                         8@MS  ri;iiiiiiiiir.                                                     ',
            \ '                                                         ZW0MZ  ;;;i;iiiii;;,                                                     ',
            \ '                                                         BB88M0  ;;iiii;iiir:                                                     ',
            \ '                                                        i@0Z88@B  ;;;iiiii;;;                                                     ',
            \ '                                                        BB88Z88@B  ;;;iiiiiir,                                                    ',
            \ '                                                       ZM88Z8Z88@B  :;;iiiii;;.                                                   ',
            \ '                                                    ;.:M08Z8Z8Z88WB   ;ri;iii;r:                                                  ',
            \ '                                                  .0Z 8W8Z8Z8Z8Z88W@r  .;;;i;i;r;                                                 ',
            \ '                                                iZMM  @B8ZZ8Z8Z8Z88BM0:   .ii;;;rri:                                              ',
            \ '                                          i;XS0WMWW0  MB8Z8Z8Z8Z8Z8Z0BMBS.      ..:::,                                            ',
            \ '                                          WMMM@W000W  XMB088Z8Z8Z8Z8Z88B@MW027;i,::ir28Bi                                         ',
            \ '                                           .X8@@M@@MW  ;WM@BB008080808000BWWMMMMMMMMMW2.                                          ',
            \ '                                               .iX20@Ma,.raBWM@MMMMM@M@MMM@@WW082Xi.                                              ',
            \ '                                                                                                                                  ',
\]

" config moin
"au! BufRead,BufNewFile *.moin
"    \ if getline(1) =~ '^@@ Syntax: 1\.5$' | setf moin1_5
"    \ | else | setf moin1_6 | endif

nmap <leader>fb :%!xxd -g1 <CR> :%s/^.\{9\}//g <CR> :%s/.\{18\}$//g <CR> :%s/0a *\%$//g<CR> :g/^$/d<CR> :%s/^/0x/g<CR>  :%s/ /,0x/g<CR> :1,$-1s/$/,/g<CR>

"
let g:rbpt_colorpairs = [
    \ ['brown',       'RoyalBlue3'],
    \ ['Darkblue',    'SeaGreen3'],
    \ ['darkgray',    'DarkOrchid3'],
    \ ['darkgreen',   'firebrick3'],
    \ ['darkcyan',    'RoyalBlue3'],
    \ ['darkred',     'SeaGreen3'],
    \ ['darkmagenta', 'DarkOrchid3'],
    \ ['brown',       'firebrick3'],
    \ ['gray',        'RoyalBlue3'],
    \ ['black',       'SeaGreen3'],
    \ ['darkmagenta', 'DarkOrchid3'],
    \ ['Darkblue',    'firebrick3'],
    \ ['darkgreen',   'RoyalBlue3'],
    \ ['darkcyan',    'SeaGreen3'],
    \ ['darkred',     'DarkOrchid3'],
    \ ['red',         'firebrick3'],
    \ ]

let g:rbpt_max = 16
let g:rbpt_loadcmd_toggle = 0
au VimEnter * RainbowParenthesesToggle
au Syntax * RainbowParenthesesLoadRound
au Syntax * RainbowParenthesesLoadSquare
au Syntax * RainbowParenthesesLoadBraces

" for ycm
let g:ycm_error_symbol = '>>'
let g:ycm_warning_symbol = '>*'
nnoremap <leader>gl :YcmCompleter GoToDeclaration<CR>
nnoremap <leader>gf :YcmCompleter GoToDefinition<CR>
nnoremap <leader>gg :YcmCompleter GoToDefinitionElseDeclaration<CR>
nmap <F4> :YcmDiags<CR>


" MiniBufExpl  config
:let g:did_minibufexplorer_syntax_inits = 1
hi MBENormal               ctermfg=223  guifg=#808080 guibg=fg
hi MBEChanged              ctermfg=202 guifg=#CD5907 guibg=fg
hi MBEVisibleNormal        ctermfg=202 guifg=#5DC2D6 guibg=fg
hi MBEVisibleChanged       ctermfg=215  guifg=#F1266F guibg=fg
hi MBEVisibleActiveNormal  ctermfg=202 guifg=#A6DB29 guibg=fg
hi MBEVisibleActiveChanged ctermfg=228 guifg=#F1266F guibg=fg

noremap <C-J>     <C-W>j
noremap <C-K>     <C-W>k
noremap <C-H>     <C-W>h
noremap <C-L>     <C-W>l

noremap <C-Down>  <C-W>j
noremap <C-Up>    <C-W>k
noremap <C-Left>  <C-W>h
noremap <C-Right> <C-W>l

let g:miniBufExplMapWindowNavVim = 1
let g:miniBufExplMapWindowNavArrows = 1
let g:miniBufExplMapCTabSwitchBufs = 1
let g:miniBufExplModSelTarget = 1



" NERDTree config
noremap <leader>nf :NERDTreeFind<CR>

" gundo config
nnoremap <F6> :GundoToggle<CR>

" vim-bookmarks config
let g:bookmark_sign = '♥'
let g:bookmark_highlight_lines = 1
highlight BookmarkSign ctermbg=166 ctermfg=89
highlight BookmarkAnnotationSign ctermbg=30  ctermfg=89
highlight BookmarkLine ctermbg=166 ctermfg=NONE
highlight BookmarkAnnotationLine ctermbg=30  ctermfg=NONE
