class getTheGinie:
    def __init__(self):
        pass
    
    def grantMyWish(self, trainX, trainY):
        
        '''
        
        input : (list, list)
        output : (int, int)   
        
        This function returns the column and threshold with minimum gini value 
        for a given data.
        
        '''
        lamp = {}
        
        rows = len(trainX)
        colm_trainX = list(zip(*trainX))
        
        for i, colm in enumerate(colm_trainX):
            for split_index in range(0, rows, 1):
                
                left_trainY, right_trainY = [], []
                
                split_val = colm[split_index]
                
                for j, val in enumerate(colm):
                    if val < split_val:
                        left_trainY.append(trainY[j])
                    else:
                        right_trainY.append(trainY[j])
                
                lsize = len(left_trainY)
                rsize = len(right_trainY)
                
                lp = sum([1 if lab == -1 else 0 for lab in left_trainY])
                rp = sum([1 if lab == -1 else 0 for lab in right_trainY])

                if lsize == 0:
                    term1 = 0
                else:
                    lterm_1 = lsize/rows
                    lterm_2 = lp/lsize
                    lterm_3 = 1 - (lp/lsize)
                    
                    term1 = lterm_1 * lterm_2 * lterm_3
                
                if rsize == 0:
                    term2 = 0
                else:
                    rterm_1 = rsize/rows
                    rterm_2 = rp/rsize
                    rterm_3 = 1 - (rp/rsize)
                    
                    term2 = rterm_1 * rterm_2 * rterm_3
                
                ginie =  term1 + term2
                print("gini: ",ginie)
                left_trainX = []
                for val in colm:
                    if val < split_val:
                        left_trainX.append(val)
                
                if len(left_trainX) != 0:
                    left_max = max(left_trainX)
                else:
                    left_max = split_val
                
                main_split = (left_max + split_val)/2
                
                if ginie not in lamp.keys():
                    lamp[ginie] = [[i, main_split]]
                else:
                    lamp[ginie].append([i, main_split])

        wish = min(lamp.keys())
        
        return lamp[wish]