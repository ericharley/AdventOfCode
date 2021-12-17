use strict;

use List::Util qw( min max sum );

use Memoize;
memoize('f');


my @n;
my %a;

while(<>)
{
	push @n, int($_);
	$a{int($_)} = 1;
}
$a{0} = 1;

@n = sort {$a <=> $b} @n;

my $max_output = 3 + max @n;

unshift @n, 0;
push @n, $max_output;


my %h;
$h{1} = 0;
$h{3} = 0;

for (my $i = 1; $i <= $#n; $i++)
{
	my $diff = $n[$i] - $n[$i - 1];
	$h{$diff}++;
}

my $p = $h{1}*$h{3};
print "1: $h{1}, 2: $h{2}, 3: $h{3}, 1*3: $p\n";


sub f
{
	my $i = shift;

	# how many ways to get to $i;

	return 0 if $i < 0 ;
	return 1 if $i == 0 ;
	return ( int($a{$i - 1})*f($i - 1) + int($a{$i - 2})*f($i - 2) + int($a{$i - 3})*f($i - 3) );
}

my $eh = f($max_output);
print "$eh\n";
