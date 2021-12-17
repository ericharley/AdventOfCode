#!/opt/local/bin/perl

$/ = "\n\n";

use JSON;

@fields = qw(byr iyr eyr hgt hcl ecl pid cid);

$c = 0;
while(<>)
{
	chomp;
	s/\n/ /g;
	%h = split /[ :]/;

	$v = 1;
   foreach $f (@fields)
	{
		$v = 0 unless exists $h{$f} || $f eq "cid";
	}

	$v = 0 unless (
		$h{"byr"} =~ /^[0-9]{4}$/
	&&
		1920 <= $h{"byr"} && $h{"byr"} <= 2002
	&&

		$h{"iyr"} =~ /^[0-9]{4}$/
	&&
		2010 <= $h{"iyr"} && $h{"iyr"} <= 2020
	&&

		$h{"eyr"} =~ /^[0-9]{4}$/
	&&

		2020 <= $h{"eyr"} && $h{"eyr"} <= 2030
	);

	$v = 0 unless $h{"hgt"} =~ /^[0-9]+(cm|in)$/;
	$v = 0 unless ($1 eq "cm") ? (150 <= $h{"hgt"} && $h{"hgt"} <= 193) : 59 <= $h{"hgt"} && $h{"hgt"} <= 76;

	$v = 0 unless $h{"hcl"} =~ /^#[0-9a-f]{6}$/;
	$v = 0 unless $h{"ecl"} =~ /^(amb|blu|brn|gry|grn|hzl|oth)$/;
	$v = 0 unless $h{"pid"} =~ /^[0-9]{9}$/;

	$c += $v;
	
}
print "$c\n";
