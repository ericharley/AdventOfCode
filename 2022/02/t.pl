use strict;

my %a;
my %m;

# 0:Lose
# 3:Draw
# 6:Win

# You		
# A:Rock       #Me
$a{"A,X"} = 3; #X:Rock
$a{"A,Y"} = 6; #Y:Paper
$a{"A,Z"} = 0; #Z:Scissors

# B:Paper
$a{"B,X"} = 0; #X:Rock
$a{"B,Y"} = 3; #Y:Paper
$a{"B,Z"} = 6; #Z:Scissors

# C:Scissors
$a{"C,X"} = 6; #X:Rock
$a{"C,Y"} = 0; #Y:Paper
$a{"C,Z"} = 3; #Z:Scissors

$m{"X"} = 1;
$m{"Y"} = 2;
$m{"Z"} = 3;

my $t = 0;

while(<>)
{
	chomp;
	my ($you, $me) = split / /;
	$t += $a{"$you,$me"} + $m{"$me"};
}
print "$t\n";
