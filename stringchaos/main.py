from stringchaos.core import useless


if __name__ == '__main__':
    u = useless.Useless()
    q = 'L1B1D2D2E2R2Q1E2F2D2B0S0'
    r = u.query(q)
    print(r)
