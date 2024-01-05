#!/opt/local/bin/perl

use strict;

my @list;

while(<>)
{
  chomp;
  push @list, [split //];
}

my $r = $#list + 1;
my $c = (scalar @{$list[0]});

my $count = 0;
for (my $i = 0, my $j = 0; $i < $r; $i++, $j+=3)
{
  $count++ if $list[$i][$j % $c] eq "#";
}
print "$count\n";
