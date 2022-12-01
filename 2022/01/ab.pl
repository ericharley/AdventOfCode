#!/usr/bin/perl
use v5.10;
use strict;
use List::Util qw/sum/;

$/ = "\n\n";

my @ns = (sort {$b <=> $a} map { sum(split /\n/) } <>)[0..2];

say $ns[0];
say sum(@ns);
