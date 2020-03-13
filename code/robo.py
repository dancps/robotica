def getElementarMatrix(a,alpha,d,theta):
    c_theta = np.cos(theta)
    s_theta = np.sin(theta)
    c_alpha = np.cos(alpha)
    s_alpha = np.sin(alpha)

    matrix = np.array([
        [c_theta,-s_theta*c_alpha,s_theta*s_alpha,a*c_theta],
        [s_theta,c_theta*c_alpha,-c_theta*s_alpha,a*s_theta],
        [0,s_alpha,c_alpha,d],
        [0,0,0,1]
    ])

    return matrix