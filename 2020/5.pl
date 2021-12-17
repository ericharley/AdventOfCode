#!/opt/local/bin/perl

$maxID = 0;
$minID = 9999999999;

%h = {};

while(<>)
{
	chomp;
	tr/FBLR/0101/;

	@f = split //;
	$t = pop @f;
	$s = pop @f;
	$r = pop @f;

	$row  = oct("0b".(join "", @f));
	$seat = oct("0b$r$s$t");
   $ID = $row * 8 + $seat;

	$a = join ",", @f;
#	print "$_ -> |$a|:$r$s$t -> $row:$seat -> $ID\n";

	$h{$ID} = 1;

	$maxID = $ID if $ID > $maxID;
	$minID = $ID if $ID < $minID;
}

print "$maxID\n";
# print "$minID\n";

for ($i = $minID; $i < $maxID; $i++)
{
	print "$i\n" if ! exists $h{$i} && exists $h{$i+1} && exists $h{$i-1};
}

