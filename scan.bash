curl -X POST https://api.metadefender.com/v4/file \
-H 'apikey: a00a79613aade8e8c086b1663e1731c1' \
-H 'content-type: multipart/form-data' \
-F =@$1 > files/1.txt

