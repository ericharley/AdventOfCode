use strict;

use List::Util qw( min max sum );

my @n;

while(<>)
{
	chomp;
	push @n, int($_);
}

my $t = 1038347917;

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
			print "$sum\n";
		}
	}
}
