use strict;

my %a;
my %m;

# 0:Lose
# 3:Draw
# 6:Win

# X:Lose
# Y:Draw
# Z:Win

# Rock: 1
# Paper: 2
# Scissors: 3

# You		
# A:Rock       #Me
$a{"A,X"} = 3; #X:Lose -> Scissors
$a{"A,Y"} = 1; #Y:Draw -> Rock
$a{"A,Z"} = 2; #Z:Win  -> Paper

# B:Paper
$a{"B,X"} = 1; #X:Lose -> Rock
$a{"B,Y"} = 2; #Y:Draw -> Paper
$a{"B,Z"} = 3; #Z:Win  -> Scissors

# C:Scissors
$a{"C,X"} = 2; #X:Lose -> Paper
$a{"C,Y"} = 3; #Y:Draw -> Scissors
$a{"C,Z"} = 1; #Z:Win  -> Rock

$m{"X"} = 0;
$m{"Y"} = 3;
$m{"Z"} = 6;

my $t = 0;

while(<>)
{
	chomp;
	my ($you, $me) = split / /;
	$t += $a{"$you,$me"} + $m{$me};
}
print "$t\n";
