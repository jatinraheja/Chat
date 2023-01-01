import uvicorn


def main():
    uvicorn.run("src:app", reload=True)


if __name__ == '__main__':
    main()
