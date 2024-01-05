#!/opt/local/bin/perl

# acc
# jmp
# nop

# acc increases or decreases a single global value called the accumulator by the value given in the argument. For example, 
# acc +7 would increase the accumulator by 7. The accumulator starts at 0. After an acc instruction, the instruction 
# immediately below it is executed next.

# jmp jumps to a new instruction relative to itself. The next instruction to execute is found using the argument as an 
# offset from the jmp instruction; for example, jmp +2 would skip the next instruction, jmp +1 would continue to the 
# instruction immediately below it, and jmp -20 would cause the instruction 20 lines above to be executed next.

# nop stands for No OPeration - it does nothing. The instruction immediately below it is executed next.

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

#my $program_length = scalar @program;
#for (my $i = 0; $i < $program_length; $i++)
#{
#	# my ($op, $sign, $val) = @{$program[$i]};
#	my @tuple = @{$program[$i]};
#	my $op = $tuple[0];
#	my $sign = $tuple[1];
#	my $val = $tuple[2];
#	print "$op, $sign, $val\n";
#	if ($op eq "jmp")
#	{
#		${$program[$i]}[0] = "nop";
#		my $ret = doit(\@program);
##		print "$ret\n" if $ret =~ /HALT/;
#		print "$ret\n";
#		${$program[$i]}[0] = "jmp";
#	}
#
#	if ($op eq "nop")
#	{
#		@{$program[$i]} = ["jmp", $sign, $val];
#		my $ret = doit(\@program);
##		print "$ret\n" if $ret =~ /HALT/;
#		print "$ret\n";
#		@{$program[$i]} = ["nop", $sign, $val];
#	}
#}


sub doit
{
	my @program = @{$_[0]};

	my $program_length = scalar @program;

	my $instruction_count = 0;
	my $acc = 0;
	my $pc = 0;
	my %hit;
	while(1)
	{
		$instruction_count++;
	
		my @tuple = @{$program[$pc]};
		my $op = $tuple[0];
		my $sign = $tuple[1];
		my $val = $tuple[2];
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
			print "$op : ";
			return "HALT : PC = $pc, ACC = $acc";
		}
	
		if ($hit{$pc} == 1)
		{
			return "INFINITE LOOP DETECTED: PC = $pc, ACC = $acc";
		}
	}
	die;
}
