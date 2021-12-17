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

my @a = ([1,1], [3,1], [5,1], [7,1], [1,2]);

my $prod = 1;
foreach my $b (@a)
{
	my @c = @{$b};
	my $right = $c[0];
	my $down = $c[1];
	my $count = 0;
	for (my $i = 0, my $j = 0; $i < $r; $i+=$down, $j+=$right)
	{
	   $count++ if $list[$i][$j % $c] eq "#";
	}
	
	$prod *= $count;
}
print "$prod\n";
