# 2.4. Инструменты Git

### 1) Найдите полный хеш и комментарий коммита, хеш которого начинается на aefea.
      
      aefead2207ef7e2aa5dc81a34aedf0cad4c32545
      Update CHANGELOG.md

### 2) Какому тегу соответствует коммит 85024d3?
      
      v0.12.23

### 3) Сколько родителей у коммита b8d720? Напишите их хеши.
     
      b8d720f8340221f2146e4e4870bf2ee0bc48f2d5
      его предки
      1 - 56cd7859e05c36c06b56d013b55a252d0bb7e158
      2 - 9ea88f22fc6269854151c571162c5bcf958bee2b
      (прородители)
      1.1 - 58dcac4b798f0a2421170d84e507a42838101648
      1.2 - ffbcf55817cb96f6d5ffe1a34abe963b159bf34e
      

### 4) Перечислите хеши и комментарии всех коммитов которые были сделаны между тегами v0.12.23 и v0.12.24.
      
     33ff1c03b (tag: v0.12.24) v0.12.24
     b14b74c49 [Website] vmc provider links
     3f235065b Update CHANGELOG.md
     6ae64e247 registry: Fix panic when server is unreachable
     5c619ca1b website: Remove links to the getting started guide's old location
     06275647e Update CHANGELOG.md
     d5f9411f5 command: Fix bug when using terraform login on Windows
     4b6d06cc5 Update CHANGELOG.md
     dd01a3507 Update CHANGELOG.md
     225466bc3 Cleanup after v0.12.23 release

### 5) Найдите коммит в котором была создана функция func providerSource, ее определение в коде выглядит так func providerSource(...)(вместо троеточего перечислены аргументы).
      
      8c928e83589d90a031f811fae52a81be7153e82f

### 6) Найдите все коммиты в которых была изменена функция globalPluginDirs
      
      commit 78b12205587fe839f10d946ea3fdc06719decb05
      Author: Pam Selle <204372+pselle@users.noreply.github.com>
      Date:   Mon Jan 13 16:50:05 2020 -0500

      commit 52dbf94834cb970b510f2fba853a5b49ad9b1a46
      Author: James Bardin <j.bardin@gmail.com>
      Date:   Wed Aug 9 17:46:49 2017 -0400

      commit 41ab0aef7a0fe030e84018973a64135b11abcd70
      Author: James Bardin <j.bardin@gmail.com>
      Date:   Wed Aug 9 10:34:11 2017 -0400

      commit 66ebff90cdfaa6938f26f908c7ebad8d547fea17
      Author: James Bardin <j.bardin@gmail.com>
      Date:   Wed May 3 22:24:51 2017 -0400

      commit 8364383c359a6b738a436d1b7745ccdce178df47
      Author: Martin Atkins <mart@degeneration.co.uk>
      Date:   Thu Apr 13 18:05:58 2017 -0700

### 7) Кто автор функции synchronizedWriters?

      Author: Martin Atkins <mart@degeneration.co.uk>
