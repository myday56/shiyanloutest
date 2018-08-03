set nocompatible

"æ¾ç¤ºè¡å·
set number

"è®¾ç½®å¨ç¼è¾è¿ç¨ä¸­å³ä¸è§æ¾ç¤ºåæ çè¡åä¿¡æ¯
set ruler
 
"å¨ç¶ææ æ¾ç¤ºæ­£å¨è¾å¥çå½ä»¤
set showcmd
 
"è®¾ç½®åå²è®°å½æ¡æ°
set history=1000
 
"è®¾ç½®åæ¶å¤ä»½ ç¦æ­¢ä¸´æ¶æä»¶ççæ
set nobackup
set noswapfile
 
"è®¾ç½®å¹éæ¨¡å¼,ç±»ä¼¼å½è¾å¥ä¸ä¸ªå·¦æ¬å·æ¶ä¼å¹éç¸åºçé£ä¸ªå³æ¬å·
set showmatch
 
"è®¾ç½®C/C++æ¹å¼èªå¨å¯¹é½
set autoindent
set cindent
 
"å¼å¯è¯­æ³é«äº®åè½
syntax enable
syntax on
 
"æå®éè²æ¹æ¡ä¸º256è²
set t_Co=256
 
"è®¾ç½®æç´¢æ¶å¿½ç¥å¤§å°å
set ignorecase

"å®æ¶æ¾ç¤ºæç´¢ç»æ
set incsearch
 
"éç½®backspaceçå·¥ä½æ¹å¼
set backspace=indent,eol,start
 
"è®¾ç½®å¨vimä¸­å¯ä»¥ä½¿ç¨é¼ æ 
set mouse=a
 
"è®¾ç½®tabå®½åº¦
set tabstop=4
 
"è®¾ç½®èªå¨å¯¹é½ç©ºæ ¼æ°
set shiftwidth=4
 
"è®¾ç½®éæ ¼é®æ¶å¯ä»¥å é¤4ä¸ªç©ºæ ¼
set smarttab
set softtabstop=4
 
"å°tabé®èªå¨è½¬æ¢ä¸ºç©ºæ ¼
set expandtab
 
"è®¾ç½®ç¼ç æ¹å¼
set encoding=utf-8
 
"èªå¨å¤æ­ç¼ç æ¶ ä¾æ¬¡å°è¯ä»¥ä¸ç¼ç 
set fileencodings=ucs-bom,utf-8,cp936,gb18030,big5,euc-jp,euc-kr,latin1
 
"æ£æµæä»¶ç±»å
filetype on
 
"éå¯¹ä¸åçæä»¶éåä¸åçç¼©è¿æ¹å¼
filetype indent on
 
"å¯å¨æºè½è¡¥å¨
filetype plugin indent on

"æ¬å·èªå¨è¡¥å¨
inoremap ( ()<ESC>i
inoremap [ []<ESC>i
inoremap { {}<ESC>i
inoremap < <><ESC>i
