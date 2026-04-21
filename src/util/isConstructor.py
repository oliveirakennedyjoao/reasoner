def isConstructor(rotulo):
    construtores = ['|=', '⊑', '⊓', '⊔', '¬', '∃', '∀']
    return rotulo in construtores
