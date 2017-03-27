" NS_PRE_INSTALL
set list
set listchars=tab:>-,trail:-
au BufRead,BufNewFile *.conf set ft=dosini
hi Comment ctermfg=6
set nocompatible
syntax enable
syntax on
colorscheme desert
" au BufRead,BufNewFile *.py
" \ set tabstop=4
" \ set softtabstop=4
" \ set shiftwidth=4
" \ set textwidth=79
" \ set expandtab
" \ set autoindent
" \ set fileformat=unix
" au BufNewFile,BufRead *.py,*.pyw setf python
set autoindent " same level indent
set smartindent " next level indent
" indent I fuck DOG
" set expandtab
" set tabstop=8
" set shiftwidth=4
" set softtabstop=4
" 设置 字体 大小
set guifont=Consolas:h12
" 设置 前端显示行数
set number
" 设置 编码格式
set encoding=utf-8
set fileencoding=utf-8
set fileencodings=ucs-bom,utf-8,gbk
" 利用 \ 转义掉 Program Files 之间 の 空格
" http://blog.csdn.net/neofung/article/details/6580580
" http://vi.stackexchange.com/questions/5339/how-to-deal-with-string-containing-spaces-in-vim-script
" 设置 shell
" 设置 文件类型识别?
filetype plugin indent on
inoremap ( ()<ESC>i
inoremap [ []<ESC>i
inoremap { {}<ESC>i
inoremap < <><ESC>i
inoremap ' ''<ESC>i
inoremap " ""<ESC>i
" -------------------------------
" For Vundle
filetype off " for markdown
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" Plugin '插件名'
Plugin 'VundleVim/Vundle.vim'
" 文件树
Plugin 'scrooloose/nerdtree'
" 自动补全
" Plugin 'Valloric/YouCompleteMe'
" 多光标实现
Plugin 'terryma/vim-multiple-cursors'
" multiple-cursors 插件设置
let g:multi_cursor_next_key='<C-n>'
let g:multi_cursor_prev_key='<C-p>'
let g:multi_cursor_skip_key='<C-x>'
let g:multi_cursor_quit_key='<Esc>'
" Gvim 支持 多光标
" https://github.com/terryma/vim-multiple-cursors#faq
set selection=inclusive
highlight multiple_cursors_cursor term=reverse cterm=reverse gui=reverse
highlight link multiple_cursors_visual Visual
" 代码浏览 (IDE)
Plugin 'taglist.vim'
" taglist 插件设置
" map <F11> :!ctags -R --c++-kinds=+p --fields=+iaS --extra=+q .<CR><CR> :TlistUpdate<CR>
" imap <F11><ESC>:!ctags -R --c++-kinds=+p --fields=+iaS --extra=+q .<CR><CR> :TlistUpdate<CR>
" set tags=tags
" set tags+=./tags
" 按F11生成个人tags
" noremap <F11> :!ctags -R --c++-kinds=+p --fields=+iaS --extra=+q -f ~/.vim/tags/tags_self<CR>
" 以上方法就是 将 ctags 生成 の tags 文件 放在当前目录下 改文件记录 所有 需要
" tags の 所有 lang
" set tags=tags
" set tags+=~/.vim/tags/tags_self,~/.vim/tags/
" noremap <F11> :!ctags -R -o ~/.vim/tags/tags_self --Python-kinds=-i --fields=+iaS<CR>
" 怎么改都没成功 将 输出 の tags 文件 放在其他位置
noremap <F11> :!ctags -R . --Python-kinds=-i --fields=+iaS<CR>
" 设置tags路径,F11 自动加载到 个人定义 tags(√) 但 使用 Ctrl+] 不能正确找到 对应位置
let Tlist_Ctags_Cmd='/usr/bin/ctags'
let Tlist_Show_One_File=1   " 不同时显示多个文件的tag，只显示当前文件的
let Tlist_WinWidt =28       " 设置taglist的宽度
let Tlist_Exit_OnlyWindow=1 " 如果taglist窗口是最后一个窗口，则退出vim
let Tlist_Use_Right_Window=1    " 在右侧窗口中显示taglist窗口
" let Tlist_Use_Left_Windo =1   " 在左侧窗口中显示taglist窗口
" 快速注释
Plugin 'scrooloose/nerdcommenter'
let g:NERDSpaceDelims = 1
let g:NERDCompactSexyComs = 1
let g:NERDDefaultAlign = 'left'
let g:NERDCustomDelimiters = { 'c': { 'left': '/**','right': '*/' } }
let g:NERDCommentEmptyLines = 1
let g:NERDTrimTrailingWhitespace = 1
" 美化状态栏
Plugin 'bling/vim-airline'
" airline 设置
let g:airline_left_sep='>'
let g:airline_detect_modified=1
let g:airline_detect_paste=1
let g:airline_detect_crypt=1
let g:airline_detect_spell=1
let g:airline_detect_iminsert=0
" 多种括号补全
Plugin 'tpope/vim-surround'
" shentm 知道 这到底怎么用了
" 在 normal mode 下
" cs'" 	# 将 包含 の ' 替换成 "
" ds'  	# 将 包含 の ' 删除掉
" yss(	# 主动为 多个 单词 添加 ()
" ysiw{	# 单个 单词 带空格 の 包含 {}
" ysiw}	# 不带空格 の 包含{}
" MarkDown 支持
Plugin 'plasticboy/vim-markdown'
" markdown 设置
let g:vim_markdown_folding_disabled = 1
let g:vim_markdown_folding_style_pythonic = 1
let g:vim_markdown_folding_level = 6
let g:vim_markdown_no_default_key_mappings = 1
let g:vim_markdown_frontmatter = 1
let g:vim_markdown_override_foldtext = 0
" filetype plugin indent on " for markdown 2017年3月27日09:30:44 好扯 cm
" Python mode I fuck DOG too
" Plugin 'python-mode/python-mode'
" snippets 支持
Plugin 'SirVer/ultisnips'
Plugin 'honza/vim-snippets'
let g:UltiSnipsExpandTrigger='<tab>'
let g:UltiSnipsJumpForwardTrigger='<c-b>'
let g:UltiSnipsJumpBackwardTrigger='<c-z>'
" 这里号吉尔扯 不成功 Python 一直报错 rm -rf UltiSnips
" let g:UltiSnipsSnippetDirectories=['UltiSnips', '~/.vim/UltiSnips']
" let g:UltiSnipsSnippetsDir = '~/.vim/UltiSnips'
let g:UltiSnipsListSnippets = '<C-Tab>'
" let g:UltiSnipsJumpForwardTrigger = '<Tab>'
" let g:UltiSnipsJumpBackwardTrigger = '<S-Tab>'
call vundle#end()
filetype plugin indent on " cm 掉 markdown 在此再添加

"
" 简要帮助文档
" :PluginList       - 列出所有已配置的插件
" :PluginInstall    - 安装插件,追加 `!` 用以更新或使用 :PluginUpdate
" :PluginSearch foo - 搜索 foo ; 追加 `!` 清除本地缓存
" :PluginClean      - 清除未使用插件,需要确认; 追加 `!` 自动批准移除未使用插件
