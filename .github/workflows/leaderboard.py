import json
import os
import urllib.request
import ssl


ITBENCH_API = os.getenv("ITBENCH_API")
ITBENCH_API_TOKEN = os.getenv("ITBENCH_API_TOKEN")
ITBENCH_CERT = os.getenv("ITBENCH_CERT")


def get_leaderboard():
    # Required as the current IT Bench server is not using a trusted certificate
    ssl_context = ssl.create_default_context(cafile=ITBENCH_CERT)
    url = f"{ITBENCH_API}/registry/aggregate-results"
    headers = {
        "Authorization" : f"Bearer {ITBENCH_API_TOKEN}"
    }
    req = urllib.request.Request(url=url, headers=headers, method="GET")
    res = urllib.request.urlopen(req, timeout=10, context=ssl_context)
    
    if res.getcode() != 200:
        print(f"Error requesting leaderboard JSON: {res.status_code}. {res.content}")
        exit(1)

    res_body = res.read()
    res_dict = json.loads(res_body.decode("utf-8"))
    return res_dict



def print_table(data):
    header_str = ['Agent', 'Benchmark', 'Scenario Category', '% Resolved', 'Mean Processing Time', 'Passed', 'Date']
    line_fmt = '| {:^13} | {:^13} | {:^23} | {:^13} | {:^13} | {:^13} | {:^13} |'
    headers = line_fmt.format(*header_str)
    header_len = len(headers)
    print('-' * header_len)
    print(headers)
    print('-' * header_len)
    for bench_line in data:
        print(line_fmt.format(*bench_line))


if __name__ == "__main__":
   
    leaderboard = get_leaderboard()
    bench_summary = []
    for benchmark in leaderboard:
        #print(benchmark)
        bench_line = [
            benchmark["agent"],
            benchmark["name"],
            benchmark["incident_type"],
            int((benchmark["num_of_passed"] / len(benchmark["results"]))*100),
            benchmark["mttr"],
            benchmark["num_of_passed"],
            benchmark["date"]
        ]

        bench_summary.append(bench_line)


    print_table(bench_summary)