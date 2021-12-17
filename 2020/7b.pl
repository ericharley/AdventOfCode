use strict;

my %vertices;
my %edges;
my %weights;

while(<>)
{
	chomp;
	my $str = $_;

	$str =~ s/ bags//g;
	$str =~ s/ bag//g;
	$str =~ s/.$//;
	
 	my ($left,$right) = split / contain /, $str;
	my @contains = split /, /, $right;

	$vertices{$left} = 1;

	foreach my $right (@contains)
	{
		$right =~ s/^([0-9]+) //;
		my $weight = $1;
      $weight = 0 if $weight eq "";

		$vertices{$right} = 1;

		push( @{ $edges { $left } }, $right);
		$weights{"$left:$right"} = $weight;
	}
}

print (works("shiny gold") - 1);
print "\n";

sub works
{
	my $bag_color = shift;
	return 1 if $bag_color eq "no other";

	my @neighbors = @{ $edges {$bag_color} } if exists $edges {$bag_color};
	my $sum = 1;
	foreach my $v ( @neighbors )
	{
		$sum += $weights{"$bag_color:$v"}*works($v);
	}
	return $sum;
}
