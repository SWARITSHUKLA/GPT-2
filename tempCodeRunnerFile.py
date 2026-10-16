tt = (q@k.transpose(-2,-1)) * (1.0 / math.sqrt(k.size(-1)))
        # att = att.masked_fill(self.bias[:,:,:T,:T]== 0, float('-inf'))
        # att = F.softmax(att,dim = -1)
        # y = att @ v