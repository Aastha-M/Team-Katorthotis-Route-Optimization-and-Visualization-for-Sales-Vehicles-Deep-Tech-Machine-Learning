function [c,cw,id_c,id_cw]=dis_rec(sale_points,weight,n)
    %% Direct kmeans
    [id_c,c]=kmeans(sale_points,n);
    %% Weighted Kmeans
    %Duplicating points based of weight
    sp_w=[];
    for i=1:length(weight)
        nn=weight(i);
        el=sale_points(i,:);
        for j=1:length(nn)
            sp_w=[sp_w;el];
        end
    end
    [id_cw,cw]=kmeans(sp_w,n)
end    