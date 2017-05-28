class Object
    def implies?(obj)
        obj
    end

    def not_implies?(obj)
        false
    end

    def xnor(obj)
        obj
    end

    def nand(obj)
        !obj
    end

    def nor(obj)
        false
    end
end

class FalseClass
    def implies?(obj)
        true
    end

    def not_implies?(obj)
        !obj
    end

    def xnor(obj)
        !obj
    end

    def nand(obj)
        true
    end

    def nor(obj)
        !obj
    end
end

class NilClass
    def implies?(obj)
        true
    end

    def not_implies?(obj)
        !obj
    end

    def xnor(obj)
        !obj
    end

    def nand(obj)
        true
    end

    def nor(obj)
        !obj
    end
end
