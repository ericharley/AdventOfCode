#!/opt/local/bin/perl

use strict;

my @program;

while(<>)
{
	chomp;
	die unless /^(acc|jmp|nop) (.)([0-9]+)$/;
	my $op = $1;
	my $sign = $2;
	my $val = $3;

	push @program, [$op, $sign, $val];
}

my $ret = doit(\@program);
print "$ret\n";

my $program_length = scalar @program;
for (my $i = 0; $i < $program_length; $i++)
{
	my ($op, $sign, $val) = @{$program[$i]};
#	print "$op, $sign, $val\n";
	if ($op eq "jmp")
	{
		${$program[$i]}[0] = "nop";
		my $ret = doit(\@program);
		print "$ret\n" if $ret =~ /^OUT OF BOUNDS/;
		${$program[$i]}[0] = "jmp";
	}

	if ($op eq "nop")
	{
		${$program[$i]}[0] = "jmp";
		my $ret = doit(\@program);
		print "$ret\n" if $ret =~ /^OUT OF BOUNDS/;
		${$program[$i]}[0] = "nop";
	}
}


sub doit
{
	my @program = @{$_[0]};

	my $program_length = scalar @program;

	my $instruction_count = 0;
	my $acc = 0;
	my $pc = 0;
	my %hit;
	while($pc < $program_length)
	{
		my ($op, $sign, $val) = @{$program[$pc]};

		$hit{$pc} = 1;
	
		if ($op eq "nop")
		{
			# do nothing
			$pc++;
		}
		elsif ($op eq "jmp")
		{
			$pc += int("$sign$val");
		}
		elsif ($op eq "acc")
		{
			$acc += int("$sign$val");
			$pc++;
		}
		else
		{
			return "ILLEGAL INSTRUCTION \"$op\": PC = $pc, ACC = $acc";
		}
	
		if ($hit{$pc} == 1)
		{
			return "INFINITE LOOP DETECTED: PC = $pc, ACC = $acc";
		}
	}
	return "OUT OF BOUNDS: PC = $pc, ACC = $acc";
}
