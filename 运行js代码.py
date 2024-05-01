import execjs

if __name__ == '__main__':
    print(execjs.get().name)
    js_code = """function add(a,b){
    return a+b;
}"""

    context = execjs.compile(js_code)
    result = context.call("add", 2, 3)
    print(result)



