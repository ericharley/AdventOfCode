use strict;

my @n;

while(<>)
{
	chomp;
	push @n, int($_);
}

my $p = 25;

my $i, my $j, my $k;

#print "@n\n";

# skip the first $p numbers in the list as the preamble
NUMBER: for ($i = $p; $i <= $#n; $i++)
{
	# see if we can make the number at $n[$i] from two numbers 
	for ($j = $i - $p; $j < $i; $j++)
	{
		for ($k = $j + 1; $k < $i; $k++)
		{
			my $s = $n[$j] + $n[$k];
#			print "$i, $j, $k : $n[$i] =?= $n[$j] + $n[$k] : $s\n";
			next NUMBER if $s == $n[$i];
		}
	}
	die "$n[$i]\n";
}
