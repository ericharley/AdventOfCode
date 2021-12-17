use strict;

my %vertices;
my %allowable;
my %edges;

while(<>)
{
	chomp;
	my $str = $_;
#	$str = "clear crimson bags contain 3 pale aqua bags, 4 plaid magenta bags, 3 dotted beige bags, 3 dotted black bags.";

	$str =~ s/ bags//g;
	$str =~ s/ bag//g;
	$str =~ s/.$//;
	
 	my ($left,$right) = split / contain /, $str;
	$right =~ s/[0-9]+ //g;
	my @contains = split /, /, $right;
#	my $contains = join ":", @contains;
	
#	print "|$left|$contains|\n";

	foreach my $right (@contains)
	{
#		print "$left -> $right\n";
		$vertices{$left} = 1;
		$allowable{$left} = 1;
		$vertices{$right} = 1;
		push( @{ $edges { $left } }, $right);
	}
}

foreach my $v (sort keys %allowable)
{
	next if $v eq "shiny gold";
	my @neighbors;
	@neighbors = @{ $edges {$v} } if exists $edges {$v};
	
#	print "$v : @neighbors\n";
	print "$v : " . &works($v) . "\n";
}

sub works
{
	my $bag_color = shift;

	return 1 if ($bag_color eq "shiny gold");

   my @neighbors;
   @neighbors = @{ $edges {$bag_color} } if exists $edges {$bag_color};

	foreach my $v ( @neighbors )
	{
		return 1 if works($v);
	}

	return 0;
}
