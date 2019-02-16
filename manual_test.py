url_md5=$(echo "http://www.google.com"|md5sum|cut -d ' ' -f 1)
echo "$url_md5"

curl -i --write-out %{http_code} --header "Content-Type: application/json" \
    --request POST \
    --data ' {"key":"$url_md5", "value": "00432a3bfe0a75e2dd886f7df2f85701"} ' \
    http://localhost:35555/save
echo ""
curl --write-out %{http_code} http://localhost:35555/get/$url_md5
echo ""

