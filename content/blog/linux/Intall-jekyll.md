---
title: "jekyllの環境整備"
date: 2023-04-06T00:00:00+09:00
lastmod: "2023-04-06"
---
# jekyllの環境整備

## 概要

github/lab pagesでmarkdownを静的ページとして作成できるjekyllを導入する方法を記述する
jekyllの詳細はgoogleなどで検索

## 方法

以下の手順を実行

1. rubyとgemおよび必要な依存関係のPackageをインストールする。以下のリンクを参照
[インストール方法](https://www.ruby-lang.org/ja/documentation/installation/)
Ubuntuであれば以下コマンド
> sudo apt install -y ruby gem ruby-dev gcc build-essential
2. jekyllをインストール。インストール用のgemFileを入れているので、以下を実行するのみ
> sudo bundle install --path vendor/bundle 

## トラブルシューティング

### bundle installができない

####  概要

以下のようにパスワードが求められ、rootパスを入力しても変化しないことがあった

``` ruby
Using kramdown 2.4.0
Using mercenary 0.4.0
Using colorator 1.1.0
Using terminal-table 1.8.0
Using kramdown-parser-gfm 1.1.0


Your user account isn't allowed to install to the system RubyGems.
  You can cancel this installation and run:

      bundle config set --local path 'vendor/bundle'
      bundle install

  to install the gems into ./vendor/bundle/, or you can enter your password
  and install the bundled gems to RubyGems using sudo.

  Password:
```

#### 原因

sudo漏れ。以下で実行すれば通せる

> sudo bundle install

### ruby-devが足りないことによるeventmachineおよびhttp_perserでエラー

#### 概要

以下コマンド実行時に途中でパッケージエラーが発生した

> sudo bundle install

``` ruby
Gem::Ext::BuildError: ERROR: Failed to build gem native extension.

    current directory: /var/lib/gems/3.0.0/gems/eventmachine-1.2.7/ext
/usr/bin/ruby3.0 -I /usr/lib/ruby/vendor_ruby -r ./siteconf20230401-13419-pr34tr.rb extconf.rb
mkmf.rb can't find header files for ruby at /usr/lib/ruby/include/ruby.h

You might have to install separate package for the ruby development
environment, ruby-dev or ruby-devel for example.

extconf failed, exit code 1

Gem files will remain installed in /var/lib/gems/3.0.0/gems/eventmachine-1.2.7 for inspection.
Results logged to /var/lib/gems/3.0.0/extensions/x86_64-linux/3.0.0/eventmachine-1.2.7/gem_make.out

  /usr/lib/ruby/vendor_ruby/rubygems/ext/builder.rb:95:in `run'
  /usr/lib/ruby/vendor_ruby/rubygems/ext/ext_conf_builder.rb:47:in `block in build'
  /usr/lib/ruby/3.0.0/tempfile.rb:317:in `open'
  /usr/lib/ruby/vendor_ruby/rubygems/ext/ext_conf_builder.rb:26:in `build'
  /usr/lib/ruby/vendor_ruby/rubygems/ext/builder.rb:161:in `build_extension'
  /usr/lib/ruby/vendor_ruby/rubygems/ext/builder.rb:195:in `block in build_extensions'
  /usr/lib/ruby/vendor_ruby/rubygems/ext/builder.rb:192:in `each'
  /usr/lib/ruby/vendor_ruby/rubygems/ext/builder.rb:192:in `build_extensions'
  /usr/lib/ruby/vendor_ruby/rubygems/installer.rb:847:in `build_extensions'
  /usr/share/rubygems-integration/all/gems/bundler-2.3.5/lib/bundler/rubygems_gem_installer.rb:71:in `build_extensions'
  /usr/share/rubygems-integration/all/gems/bundler-2.3.5/lib/bundler/rubygems_gem_installer.rb:28:in `install'
  /usr/share/rubygems-integration/all/gems/bundler-2.3.5/lib/bundler/source/rubygems.rb:204:in `install'
  /usr/share/rubygems-integration/all/gems/bundler-2.3.5/lib/bundler/installer/gem_installer.rb:54:in `install'
/usr/share/rubygems-integration/all/gems/bundler-2.3.5/lib/bundler/installer/gem_installer.rb:16:in
`install_from_spec'
  /tall_from_spec'sr/share/rubygems-integration/all/gems/bundler-2.3.5/lib/bundler/installer/parallel_installer.rb:186:in `do_install'
/usr/share/rubygems-integration/all/gems/bundler-2.3.5/lib/bundler/installer/parallel_installer.rb:177:in `block in
worker_pool'
  /usr/share/rubygems-integration/all/gems/bundler-2.3.5/lib/bundler/worker.rb:62:in `apply_func'
  rker_pool'
  /usr/share/rubygems-integration/all/gems/bundler-2.3.5/lib/bundler/worker.rb:57:in `block in process_queue'
  /usr/share/rubygems-integration/all/gems/bundler-2.3.5/lib/bundler/worker.rb:54:in `loop'
  /usr/share/rubygems-integration/all/gems/bundler-2.3.5/lib/bundler/worker.rb:54:in `process_queue'
/usr/share/rubygems-integration/all/gems/bundler-2.3.5/lib/bundler/worker.rb:91:in `block (2 levels) in
create_threads'

An error occurred while installing eventmachine (1.2.7), and Bundler cannot continue.

In Gemfile:
  minima was resolved to 2.5.1, which depends on
    jekyll-feed was resolved to 0.17.0, which depends on
      jekyll was resolved to 4.1.1, which depends on
        em-websocket was resolved to 0.5.3, which depends on
          eventmachine


Gem::Ext::BuildError: ERROR: Failed to build gem native extension.

    current directory: /var/lib/gems/3.0.0/gems/http_parser.rb-0.8.0/ext/ruby_http_parser
/usrte_threads'/bin/ruby3.0 -I /usr/lib/ruby/vendor_ruby -r ./siteconf20230401-13419-3pwrjq.rb extconf.rb
mkmf.rb can't find header files for ruby at /usr/lib/ruby/include/ruby.hn error occurred while installing eventmachine (1.2.7), and Bundler cannot continue.
n Gemfile:
You might have to install separate package for the ruby development
environment, ruby-dev or ruby-devel for example.

extconf failed, exit code 1

Gem files will remain installed in /var/lib/gems/3.0.0/gems/http_parser.rb-0.8.0 for inspection.
Results logged to /var/lib/gems/3.0.0/extensions/x86_64-linux/3.0.0/http_parser.rb-0.8.0/gem_make.out

  ma ws resolved to 0.17.0, which depends onas resolved to 2s resolved to 4.1.1, which depends on.5.1, which ocket was resolved to 0.5.3, which depends onepends onusat  /var/lib/gems/3.0.0/extensions/x86_64-linux/3.0.0/eventmachine-1.2.7/gem_make.ourn error occurred while installing http_parser.rb (0.8.0), and Bundler cannot continue.

In Gemfile:
  minima was resolved to 2.5.1, which depends on
    jekyll-feed was resolved to 0.17.0, which depends on
      jekyll was resolved to 4.1.1, which depends on
        em-websocket was resolved to 0.5.3, which depends on
          http_parser.rb
```

エラーlogを見たところ「ruby-devがない」というログが存在していた
``` bash
$ cat /var/lib/gems/3.0.0/extensions/x86_64-linux/3.0.0/eventmachine-1.2.7/gem_make.out

current directory: /var/lib/gems/3.0.0/gems/eventmachine-1.2.7/ext
/usr/bin/ruby3.0 ry: /var/lib/gems/3.0.0/gems/eventmachine-1.2.7/extor_ruby -r ./siteconf20230401-13320-vwjw0f.rb extconf.rb
mkmf.rb can't find header files for ruby at ecking for -lcrypto... ecking for openssl/ssl.h... ecking for rb_trap_immediate in ruby.h,rubysig.h... ecking for rb_thread_blocking_region()... ecking for rb_thread_call_without_gvl() in ruby/thread.h... yecking for rb_thread_fd_select()... yecking for rb_fdset_t in ruby/intern.h... yecking for rb_wait_for_single_fd()... yecking for rb_enable_interrupt()... ecking for rb_time_new()... yecking for inotify_init() in sys/inotify.h... yecking for writev() in sys/uio.h... yecking for pipe2() in unistd.h... yecking for accept4() in sys/socket.h... yecking for SOCK_CLOEXEC in sys/socket.h... yecking for sys/event.h... ecking for epoll_create() in sys/epoll.h... yecking for clock_gettime()... yecking for CLOCK_MONOTONIC_RAW in time.h... yecking for CLOCK_MONOTONIC in time.h... yeXXFLAGS=-g -O2 -ffile-prefix-map=/build/ruby3.0-p8XSIY/ruby3.0-3.0.2=. -fstack-protector-strong -Wformat -Werror=format-security

Youting Makefile might have to install separate package for the ruby development
environment, rury-dev or ruby-devel for example.

extconf failed, exit code 1
```


#### 原因

ruby用の開発パッケージ「ruby-dev」が足りていなかった。以下で対応
> sudo apt install ruby-dev

### g++が足りないことによるeventmachineのパッケージエラー

#### 概要

以下コマンド実行時に以下のエラー
> sudo bundle install

```
Gem::Ext::BuildError: ERROR: Failed to build gem native extension.

    current directory: /var/lib/gems/3.0.0/gems/eventmachine-1.2.7/ex
TDIR\= clean
checking for -lcrypto... no
checking for openssl/ssl.h... no
checking for rb_trap_immediate in ruby.h,rubysig.h... no
checking for rb_thread_blocking_region()... no
checking for rb_thread_call_without_gvl() in ruby/thread.h... yes
checking for rb_thread_fd_select()... yes
checking for rb_fdset_t in ruby/intern.h... yes
checking for rb_wait_for_single_fd()... yes
checking for rb_enable_interrupt()... no
checking for rb_time_new()... yes
checking for inotify_init() in sys/inotify.h... yes
checking for writev() in sys/uio.h... yes
checking for pipe2() in unistd.h... yes
checking for accept4() in sys/socket.h... yes
checking for SOCK_CLOEXEC in sys/socket.h... yes
checking for sys/event.h... no
checking for epoll_create() in sys/epoll.h... yes
checking for clock_gettime()... yes
checking for CLOCK_MONOTONIC_RAW in time.h... yes
checking for CLOCK_MONOTONIC in time.h... yes
CXXFLAGS=-g -O2 -ffile-prefix-map=/build/ruby3.0-p8XSIY/ruby3.0-3.0.2=. -fstack-protector-strong -Wformat
-Werror=format-security
creating Makefile

current directory: /var/lib/gems/3.0.0/gems/eventmachine-1.2.7/ext
make DESTDIR\= clean

current directory: /var/lib/gems/3.0.0/gems/eventmachine-1.2.7/ext
make DESTDIR\=
compiling binder.cpp
make: x86_64-linux-gnu-g++: No such file or directory
make: *** [Makefile:237: binder.o] Error 127

make failed, exit code 2

Gem files will remain installed in /var/lib/gems/3.0.0/gems/eventmachine-1.2.7 for inspection.
Results logged to /var/lib/gems/3.0.0/extensions/x86_64-linux/3.0.0/eventmachine-1.2.7/gem_make.out

  /
  TDIR\ling binder.cpp=
  /usr/lib/ruby/vendor_ruby/rubygems/ext/builder.rb:36:in `each'
  /usr/lib/ruby/vendor_ruby/rubygems/ext/builder.rb:36:in `make'
  /usr/lib/ruby/vendor_ruby/rubygems/ext/ext_conf_builder.rb:63:in `block in build'
  /usr/lib/ruby/3.0.0/tempfile.rb:317:in `open'
  /usr/lib/ruby/vendor_ruby/rubygems/ext/ext_conf_builder.rb:26:in `build'
  /usr/lib/ruby/vendor_ruby/rubygems/ext/builder.rb:161:in `build_extension'
  /usr/lib/ruby/vendor_ruby/rubygems/ext/builder.rb:195:in `block in build_extensions'
  /usr/lib/ruby/vendor_ruby/rubygems/ext/builder.rb:192:in `each'
  /usr/lib/ruby/vendor_ruby/rubygems/ext/builder.rb:192:in `build_extensions'
  /usr/lib/ruby/vendor_ruby/rubygems/installer.rb:847:in `build_extensions'
  /usr/share/rubygems-integration/all/gems/bundler-2.3.5/lib/bundler/rubygems_gem_installer.rb:71:in `build_extensions'
  /usr/share/rubygems-integration/all/gems/bundler-2.3.5/lib/bundler/rubygems_gem_installer.rb:28:in `install'
  /usr/share/rubygems-integration/all/gems/bundler-2.3.5/lib/bundler/source/rubygems.rb:204:in `install'
  /usr/share/rubygems-integration/all/gems/bundler-2.3.5/lib/bundler/installer/gem_installer.rb:54:in `install'
/usr/share/rubygems-integration/all/gems/bundler-2.3.5/lib/bundler/installer/gem_installer.rb:16:in
`install_from_spec'
  /usr/share/rubygems-integration/all/gems/bundler-2.3.5/lib/bundler/installer/parallel_installer.rb:186:in `do_install'
/usr/share/rubygems-integration/all/gems/bundler-2.3.5/lib/bundler/installer/parallel_installer.rb:177:in `block in
worker_pool'
  /usr/share/rubygems-integration/all/gems/bundler-2.3.5/lib/bundler/worker.rb:62:in `apply_func'
  /usr/share/rubygems-integration/all/gems/bundler-2.3.5/lib/bundler/worker.rb:57:in `block in process_queue'
  /usr/share/rubygems-integration/all/gems/bundler-2.3.5/lib/bundler/worker.rb:54:in `loop'
  /usr/share/rubygems-integration/all/gems/bundler-2.3.5/lib/bundler/worker.rb:54:in `process_queue'
/usr/share/rubygems-integration/all/gems/bundler-2.3.5/lib/bundler/worker.rb:91:in `block (2 levels) in
create_threads'

An error occurred while installing eventmachine (1.2.7), and Bundler cannot continue.

In Gemfile:
  minima was resolved to 2.5.1, which depends on
    jekyll-feed was resolved to 0.17.0, which depends on
      jekyll was resolved to 4.1.1, which depends on
        em-websocket was resolved to 0.5.3, which depends on
          eventmachine
```

指定されているエラーログを確認したところ、以下のエラーが出ていた

```
$ cat  /var/lib/gems/3.0.0/extensions/x86_64-linux/3.0.0/eventmachine-1.2.7/gem_make.out

current directory: /var/lib/gems/3.0.0/gems/eventmachine-1.2.7/ext
/usr/bin/ruby3.0 -I /usr/lib/ruby/vendor_ruby -r ./siteconf20230401-13664-69qjw9.rb extconf.rb
checking for -lcrypto... no
checking for openssl/ssl.h... no
checking for rb_trap_immediate in ruby.h,rubysig.h... no
checking for rb_thread_blocking_region()... no
checking for rb_thread_call_without_gvl() in ruby/thread.h... yes
checking for rb_thread_fd_select()... yes
checking for rb_fdset_t in ruby/intern.h... yes
checking for rb_wait_for_single_fd()... yes
checking for rb_enable_interrupt()... no
checking for rb_time_new()... yes
checking for inotify_init() in sys/inotify.h... yes
checking for writev() in sys/uio.h... yes
checking for pipe2() in unistd.h... yes
checking for accept4() in sys/socket.h... yes
checking for SOCK_CLOEXEC in sys/socket.h... yes
checking for sys/event.h... no
checking for epoll_create() in sys/epoll.h... yes
checking for clock_gettime()... yes
checking for CLOCK_MONOTONIC_RAW in time.h... yes
checking for CLOCK_MONOTONIC in time.h... yes
CXXFLAGS=-g -O2 -ffile-prefix-map=/build/ruby3.0-p8XSIY/ruby3.0-3.0.2=. -fstack-protector-strong -Wformat -Werror=format-security
creating Makefile

current directory: /var/lib/gems/3.0.0/gems/eventmachine-1.2.7/ext
make DESTDIR\= clean

current directory: /var/lib/gems/3.0.0/gems/eventmachine-1.2.7/ext
make DESTDIR\=
compiling binder.cpp
make: x86_64-linux-gnu-g++: No such file or directory
make: *** [Makefile:237: binder.o] Error 127

make failed, exit code 2
```

#### 原因

g++のパッケージ不足。以下インストールで対応可能
> sudo apt install build-essential

### ローカルでjekyllを動かそうとした場合のエラー

#### 概要

ローカルで以下実行してjekyllを動かそうとするとエラー発生
>bundle exec jekyll serve

```
             Error: could not read file /mnt/f/Ubuntu/GitHome/enjoy/Til/_posts/0000-00-00-welcome-to-jekyll.markdown.erb: Invalid date '<%= Time.now.strftime('%Y-%m-%d %H:%M:%S %z') %>': Document '_posts/0000-00-00-welcome-to-jekyll.markdown.erb' does not have a valid date in the YAML front matter.
             ERROR: YOUR SITE COULD NOT BE BUILT:
                    ------------------------------------
                    Invalid date '<%= Time.now.strftime('%Y-%m-%d %H:%M:%S %z') %>': Document '_posts/0000-00-00-welcome-to-jekyll.markdown.erb' does not have a valid date in the YAML front matter.
                    ------------------------------------------------
      Jekyll 4.1.1   Please append `--trace` to the `serve` command
                     for any additional information or backtrace.
                    ------------------------------------------------
```

#### 原因

bundle installのパス指定漏れ + _config.xmlの設定によるもの。

bundleでのインストール時、--path指定を入れる
> sudo bundle install --path vendor/bundle 

また除外するファイルにvendorを追加する
> exclude: [vendor]


## 結論

以下の点からjekyllを入れるのは断念
- 単純にエラーが大量に出る 解決方法も追いづらい
- wsl2ではそもそも動作ができない問題が存在している
- jekyllはすでに古い模様で、hugoに移動しているリポジトリが存在していた