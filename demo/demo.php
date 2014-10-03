<?php

$instance = new SomeObject();

// lines will be joined
$instance->
  chain()->
  call();

// lines will be joined with default sublime's "join lines"
$instance->
  chain()->
  call();