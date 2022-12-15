use strict;
#use warnings;
#use 5.010;
 

my $t = 0;
while(<>)
{
	chomp;
	my $a = $_;
	#$a = "vJrwpWtwJgWrhcsFMMfFFhFp";
	my @c = split //, $a;
	#print "@c\n";
	my @h1 = @c[0..($#c/2)];
	my @h2 = @c[($#c/2 + 1)..$#c];
	
#print "@h1\n";
#print "@h2\n";

#my @intersection =
#    grep { defined }
#        @{ { map { $_ } @h1 } }
#           { map { $_ } @h2 };

	my %counts;
	++$counts{$_} for @h1;
	my @common = grep { --$counts{$_} >= 0 } @h2;
	
	#print "@common\n";
	
	for my $a (@common)
	{
		my $v = -1;
		if ($a =~ /[a-z]/)
		{
			$v = ord($a) - ord('a') + 1;
		}
		elsif ($a =~ /[A-Z]/)
		{
			$v = ord($a) - ord('A') + 27;
		} 
		print "$v\n";
		$t += $v;
		goto E;
	}
	E:
		1;
}
print "$t\n";
