use strict;

use List::Util qw( min max sum );

my @n;

while(<>)
{
	chomp;
	push @n, int($_);
}

my $t = 1038347917;

#my $s;
#my $e;

#my $sum = 0;
#for ($s = 0; $s <= $#n; $s++)
#{
#	for ($e = $s + 1; $e <= $#n; $e++)
#	{
#		$sum = sum @n[$s..$e];
#		if ($sum == $t)
#		{
#			my $min = min @n[$s..$e];
#			my $max = max @n[$s..$e];
#			my $a = $min + $max;
#			die "$s, $e, $min, $max, $a\n";
#		}
#	}
#}

my @D;
my $s;
my $k;

for ($s = 0; $s <= $#n; $s++)
{
	$D[$s][1] = $n[$s];
	for ($k = 2; $k < 1000; $k++)
	{
		$D[$s][$k] = $D[$s][$k - 1] + $n[$s + $k - 1];
		if ( $D[$s][$k] == $t )
		{
			my $min = min @n[$s .. ($s+$k - 1)];
			my $max = max @n[$s .. ($s+$k - 1)];
			my $sum = $min + $max;
#			print "$s, $k, $D[$s][$k], $n[$s + $k - 1], $min, $max, $sum\n";
			print "$sum\n";
		}
	}
}
