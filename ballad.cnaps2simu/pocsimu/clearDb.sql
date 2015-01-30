delete from cp2_mbfemsghdr;
delete from cp2_txn where DRCT = '2';
delete from cp2_hvps111 where DRCT = '2';
delete from cp2_beps121 where DRCT = '2';
commit;
