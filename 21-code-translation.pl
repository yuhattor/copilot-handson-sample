#!/usr/bin/perl
use strict;
use warnings;
use File::Spec;
use File::Basename;

print "Please enter the path to a local text file: ";
chomp(my $file_path = <STDIN>);

if ($file_path =~ /[`|;&<>(){}\[\]]/ || !File::Spec->file_name_is_absolute($file_path) && dirname($file_path) ne '.') {
    die "Invalid file path. Please provide a valid path.\n";
}
if (!-e $file_path) {
    die "File not found. Please provide an existing file path.\n";
}

open(my $fh, '<', $file_path) or die "Could not open file '$file_path': $!\n";

my $is_binary = 0;
while (read($fh, my $buffer, 1024)) {
    if ($buffer =~ /[^\x09\x0A\x0D\x20-\x7E]/) {
        $is_binary = 1;
        last;
    }
}
close($fh);

if ($is_binary) {
    die "The file '$file_path' is a binary file. Please provide a text file.\n";
}

open($fh, '<', $file_path) or die "Could not open file '$file_path': $!\n";
my $content = do { local $/; <$fh> };
close($fh);

my $word_count = scalar(split /\s+/, $content);
my $char_count = length($content);

print "The file '$file_path' contains $word_count words and $char_count characters.\n";