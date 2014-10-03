# Sublime JoinLinesEnhanced plugin

Replacement for default join_lines functionality of sublime.


### Reason

I was not satisfied how default sublime join lines worked because I often needed
to fix spaces between joining manually (add or delete). That is why this
replacement was made.


### Demo

![Demo](https://raw.github.com/shagabutdinov/sublime-join-lines-enhanced/master/demo/demo.gif "Demo")


### Installation

This plugin is part of [sublime-enhanced](http://github.com/shagabutdinov/sublime-enhanced)
plugin set. You can install sublime-enhanced and this plugin will be installed
automatically.

If you would like to install this package separately check "Installing packages
separately" section of [sublime-enhanced](http://github.com/shagabutdinov/sublime-enhanced)
package.

### Usage

  ```
  # before
  var =
    call()

  # after
  var = call()
  ```

### Commands

| Description       | Keyboard shortcut | Command palette         |
|-------------------|-------------------|-------------------------|
| Join lines        | ctrl+t            | JoinLinesEnhanced: join |